#!/usr/bin/env python3
"""
Entry Analyzer Tool
Analyzes potential trade entries against price history and provides sizing guidance.

Usage:
    uv run python entry_analyzer.py --ticker QQQ --size 15000 --conviction medium
    uv run python entry_analyzer.py --ticker QQQ --size 15000 --price 614.73
"""

import argparse
from datetime import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class PriceContext:
    """Context about current price relative to recent history"""
    current_price: float
    high_52w: float
    low_52w: float
    high_20d: float
    low_20d: float
    pct_from_52w_high: float
    pct_from_52w_low: float
    pct_from_20d_high: float
    percentile_20d: float  # Where current price sits in 20-day range (0-100)

    @property
    def is_near_high(self) -> bool:
        """Within 5% of 20-day high"""
        return self.pct_from_20d_high > -5

    @property
    def is_near_low(self) -> bool:
        """Within 5% of 20-day low"""
        return self.percentile_20d < 20

    @property
    def zone(self) -> str:
        """Classify current price zone"""
        if self.percentile_20d >= 80:
            return "OVERBOUGHT"
        elif self.percentile_20d >= 60:
            return "UPPER_RANGE"
        elif self.percentile_20d >= 40:
            return "MID_RANGE"
        elif self.percentile_20d >= 20:
            return "LOWER_RANGE"
        else:
            return "OVERSOLD"


@dataclass
class SizingRecommendation:
    """Recommended position sizing based on entry context"""
    intended_size: float
    recommended_size: float
    recommended_pct: float
    tranches: list[dict]
    warnings: list[str]
    rationale: str


def calculate_price_context(
    current_price: float,
    prices_20d: list[float],
    high_52w: float,
    low_52w: float
) -> PriceContext:
    """Calculate price context from historical data"""
    high_20d = max(prices_20d)
    low_20d = min(prices_20d)

    pct_from_52w_high = ((current_price - high_52w) / high_52w) * 100
    pct_from_52w_low = ((current_price - low_52w) / low_52w) * 100
    pct_from_20d_high = ((current_price - high_20d) / high_20d) * 100

    # Calculate percentile within 20-day range
    range_20d = high_20d - low_20d
    if range_20d > 0:
        percentile_20d = ((current_price - low_20d) / range_20d) * 100
    else:
        percentile_20d = 50

    return PriceContext(
        current_price=current_price,
        high_52w=high_52w,
        low_52w=low_52w,
        high_20d=high_20d,
        low_20d=low_20d,
        pct_from_52w_high=pct_from_52w_high,
        pct_from_52w_low=pct_from_52w_low,
        pct_from_20d_high=pct_from_20d_high,
        percentile_20d=percentile_20d
    )


def generate_sizing_recommendation(
    intended_size: float,
    price_context: PriceContext,
    conviction: str = "medium"  # low, medium, high
) -> SizingRecommendation:
    """Generate sizing recommendation based on price context and conviction"""

    warnings = []
    tranches = []

    # Base sizing multipliers
    conviction_multipliers = {
        "low": 0.5,
        "medium": 1.0,
        "high": 1.5
    }
    conv_mult = conviction_multipliers.get(conviction, 1.0)

    # Zone-based sizing
    zone = price_context.zone

    if zone == "OVERBOUGHT":
        initial_pct = 0.15 * conv_mult
        warnings.append(f"CAUTION: Price in OVERBOUGHT zone (top 20% of 20-day range)")
        warnings.append(f"Only {price_context.pct_from_20d_high:.1f}% from 20-day high")
        rationale = "Price near recent highs. Recommend minimal initial position with tranches on pullback."

        tranches = [
            {"trigger": "now", "size_pct": initial_pct, "price": price_context.current_price},
            {"trigger": "-5%", "size_pct": 0.25, "price": price_context.current_price * 0.95},
            {"trigger": "-10%", "size_pct": 0.30, "price": price_context.current_price * 0.90},
            {"trigger": "-15%", "size_pct": 0.30, "price": price_context.current_price * 0.85},
        ]

    elif zone == "UPPER_RANGE":
        initial_pct = 0.25 * conv_mult
        warnings.append(f"Price in upper range (60-80th percentile)")
        rationale = "Price elevated but not extreme. Moderate initial position."

        tranches = [
            {"trigger": "now", "size_pct": initial_pct, "price": price_context.current_price},
            {"trigger": "-5%", "size_pct": 0.25, "price": price_context.current_price * 0.95},
            {"trigger": "-10%", "size_pct": 0.25, "price": price_context.current_price * 0.90},
            {"trigger": "-15%", "size_pct": 0.25, "price": price_context.current_price * 0.85},
        ]

    elif zone == "MID_RANGE":
        initial_pct = 0.40 * conv_mult
        rationale = "Price in middle of range. Standard entry sizing."

        tranches = [
            {"trigger": "now", "size_pct": initial_pct, "price": price_context.current_price},
            {"trigger": "-5%", "size_pct": 0.30, "price": price_context.current_price * 0.95},
            {"trigger": "-10%", "size_pct": 0.30, "price": price_context.current_price * 0.90},
        ]

    elif zone == "LOWER_RANGE":
        initial_pct = 0.50 * conv_mult
        rationale = "Price in lower range. Favorable entry, larger initial position OK."

        tranches = [
            {"trigger": "now", "size_pct": initial_pct, "price": price_context.current_price},
            {"trigger": "-5%", "size_pct": 0.30, "price": price_context.current_price * 0.95},
            {"trigger": "-10%", "size_pct": 0.20, "price": price_context.current_price * 0.90},
        ]

    else:  # OVERSOLD
        initial_pct = 0.60 * conv_mult
        rationale = "Price in oversold territory. Aggressive entry warranted."

        tranches = [
            {"trigger": "now", "size_pct": initial_pct, "price": price_context.current_price},
            {"trigger": "-5%", "size_pct": 0.40, "price": price_context.current_price * 0.95},
        ]

    # Cap initial at 60% regardless of conviction
    initial_pct = min(initial_pct, 0.60)
    tranches[0]["size_pct"] = initial_pct

    # Calculate recommended size
    recommended_size = intended_size * initial_pct

    # Normalize tranches to sum to 100%
    total_pct = sum(t["size_pct"] for t in tranches)
    for t in tranches:
        t["size_pct"] = t["size_pct"] / total_pct
        t["dollar_amount"] = intended_size * t["size_pct"]

    return SizingRecommendation(
        intended_size=intended_size,
        recommended_size=recommended_size,
        recommended_pct=initial_pct,
        tranches=tranches,
        warnings=warnings,
        rationale=rationale
    )


def analyze_entry(
    ticker: str,
    intended_size: float,
    conviction: str = "medium",
    current_price: Optional[float] = None,
    prices_20d: Optional[list[float]] = None,
    high_52w: Optional[float] = None,
    low_52w: Optional[float] = None
) -> dict:
    """
    Main entry point for analyzing a potential trade entry.

    If price data not provided, uses demo data.
    In production, integrate with market data API.
    """

    # Demo data if not provided
    if not prices_20d:
        prices_20d = [
            635.77, 629.07, 632.08, 623.28, 611.67, 609.74, 623.23, 621.57,
            621.08, 608.40, 608.86, 603.66, 596.31, 599.87, 585.67, 590.07,
            605.16, 608.89, 614.73
        ]

    current_price = current_price or 614.73
    high_52w = high_52w or 637.01
    low_52w = low_52w or 420.00

    context = calculate_price_context(current_price, prices_20d, high_52w, low_52w)
    recommendation = generate_sizing_recommendation(intended_size, context, conviction)

    return {
        "ticker": ticker,
        "analysis_time": datetime.now().isoformat(),
        "price_context": {
            "current_price": context.current_price,
            "zone": context.zone,
            "percentile_20d": round(context.percentile_20d, 1),
            "pct_from_20d_high": round(context.pct_from_20d_high, 1),
            "20d_range": f"${context.low_20d:.2f} - ${context.high_20d:.2f}",
        },
        "recommendation": {
            "intended_size": f"${intended_size:,.2f}",
            "recommended_initial": f"${recommendation.recommended_size:,.2f}",
            "recommended_pct": f"{recommendation.recommended_pct:.0%}",
            "rationale": recommendation.rationale,
            "warnings": recommendation.warnings,
            "tranches": [
                {
                    "trigger": t["trigger"],
                    "size": f"${t['dollar_amount']:,.2f}",
                    "pct": f"{t['size_pct']:.0%}",
                    "target_price": f"${t['price']:.2f}" if t["trigger"] != "now" else "current"
                }
                for t in recommendation.tranches
            ]
        }
    }


def format_report(analysis: dict) -> str:
    """Format analysis as readable report"""
    lines = []
    lines.append("=" * 60)
    lines.append(f"ENTRY ANALYSIS: {analysis['ticker']}")
    lines.append(f"Time: {analysis['analysis_time']}")
    lines.append("=" * 60)
    lines.append("")

    ctx = analysis["price_context"]
    lines.append("PRICE CONTEXT:")
    lines.append(f"  Current Price: ${ctx['current_price']:.2f}")
    lines.append(f"  Zone: {ctx['zone']}")
    lines.append(f"  20-Day Percentile: {ctx['percentile_20d']}%")
    lines.append(f"  Distance from 20d High: {ctx['pct_from_20d_high']}%")
    lines.append(f"  20-Day Range: {ctx['20d_range']}")
    lines.append("")

    rec = analysis["recommendation"]
    lines.append("SIZING RECOMMENDATION:")
    lines.append(f"  Intended Position: {rec['intended_size']}")
    lines.append(f"  Recommended Initial: {rec['recommended_initial']} ({rec['recommended_pct']})")
    lines.append(f"  Rationale: {rec['rationale']}")
    lines.append("")

    if rec["warnings"]:
        lines.append("WARNINGS:")
        for w in rec["warnings"]:
            lines.append(f"  {w}")
        lines.append("")

    lines.append("ENTRY TRANCHES:")
    for i, t in enumerate(rec["tranches"], 1):
        lines.append(f"  {i}. {t['trigger']:>6}: {t['size']} ({t['pct']}) @ {t['target_price']}")

    lines.append("")
    lines.append("=" * 60)

    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze trade entry timing and sizing")
    parser.add_argument("--ticker", type=str, default="QQQ", help="Ticker symbol")
    parser.add_argument("--size", type=float, default=10000, help="Intended position size in $")
    parser.add_argument("--conviction", type=str, default="medium",
                       choices=["low", "medium", "high"], help="Conviction level")
    parser.add_argument("--price", type=float, help="Current price (optional)")

    args = parser.parse_args()

    analysis = analyze_entry(
        ticker=args.ticker,
        intended_size=args.size,
        conviction=args.conviction,
        current_price=args.price
    )
    print(format_report(analysis))
