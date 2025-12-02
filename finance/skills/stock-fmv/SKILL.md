---
name: stock-fmv
description: Calculate fair market value for stocks using multiple valuation methods (P/E, P/S, EV/EBITDA), scenario analysis with probability weighting, and clear investment recommendations. Use when analyzing stock valuations, determining if a stock is over/undervalued, or making buy/sell decisions.
license: MIT
---

# Stock Fair Market Value

Conducts comprehensive fair market value (FMV) analysis using multiple valuation methods and scenario analysis.

## When This Skill Triggers

- User asks about fair value of a stock
- User wants to know if a stock is over/undervalued
- User considering buying or selling a position
- User asks for a valuation analysis
- User wants to compare current price to intrinsic value

## Workflow

### 1. Gather Financial Data

Collect the following for the target company:

**Earnings Data:**
- Latest quarterly results (revenue, EPS, margins)
- Forward guidance (FY current, FY next)
- Analyst consensus estimates
- Key operational metrics

**Market Data:**
- Current stock price
- Market cap, enterprise value
- Recent price performance

**Peer Context:**
- Comparable company multiples
- Industry average valuations
- Growth rate comparisons

### 2. Multi-Method Valuation

Apply three valuation approaches and show all work:

#### A. P/E Multiple Approach

```
FMV = Forward EPS × Appropriate P/E Multiple

Inputs:
- FY1 EPS estimate: $X.XX
- FY2 EPS estimate: $X.XX
- Peer average P/E: XXx
- Company-specific adjustment: +/-X% (for growth, margins, risk)
- Applied multiple: XXx

Calculation:
FMV = $X.XX × XXx = $XXX.XX
```

#### B. P/S Multiple Approach

```
FMV = Revenue per Share × Appropriate P/S Multiple

Inputs:
- Revenue guidance: $XXB
- Shares outstanding: XXX M
- Revenue per share: $XX.XX
- Peer average P/S: X.Xx
- Margin-adjusted multiple: X.Xx

Calculation:
FMV = $XX.XX × X.Xx = $XXX.XX
```

#### C. EV/EBITDA Approach

```
FMV = (EBITDA × Multiple - Net Debt) / Shares

Inputs:
- EBITDA estimate: $X.XB
- Peer EV/EBITDA: XXx
- Net debt (cash): ($X.XB)
- Shares outstanding: XXX M

Calculation:
Enterprise Value = $X.XB × XXx = $XX.XB
Equity Value = $XX.XB - (-$X.XB) = $XX.XB
FMV per share = $XX.XB / XXX M = $XXX.XX
```

### 3. Blended Valuation

Combine methods with appropriate weights:

| Method | FMV | Weight | Contribution |
|--------|-----|--------|--------------|
| P/E (FY1) | $XXX | 40% | $XX.XX |
| P/S | $XXX | 30% | $XX.XX |
| EV/EBITDA | $XXX | 30% | $XX.XX |
| **Blended** | | **100%** | **$XXX.XX** |

**Fair Market Value Range:** $XXX - $XXX (±5-10%)

### 4. Scenario Analysis

Build probability-weighted scenarios:

#### Bull Case (20-35% probability)
- **Assumptions:** [Best case drivers]
- **EPS:** $X.XX (+XX% vs base)
- **Multiple:** XXx (premium for outperformance)
- **FMV:** $XXX

#### Base Case (50-60% probability)
- **Assumptions:** [Most likely outcome]
- **EPS:** $X.XX
- **Multiple:** XXx
- **FMV:** $XXX

#### Bear Case (15-25% probability)
- **Assumptions:** [Downside risks]
- **EPS:** $X.XX (-XX% vs base)
- **Multiple:** XXx (discount for underperformance)
- **FMV:** $XXX

**Probability-Weighted FMV:**
```
= (Bull × P_bull) + (Base × P_base) + (Bear × P_bear)
= ($XXX × 25%) + ($XXX × 55%) + ($XXX × 20%)
= $XXX.XX
```

### 5. Current Price Assessment

Compare market price to FMV:

```
Current Price: $XXX.XX
Fair Market Value: $XXX.XX (range: $XXX - $XXX)
Valuation Gap: +/-XX%

Market is pricing in: [Bull case / Base case / Bear case]

Implied expectations:
- Revenue growth: XX%
- Margin expansion: XX bps
- Multiple expansion/contraction: XXx → XXx
```

### 6. Investment Recommendation

Provide clear, actionable guidance:

**Rating: [BUY / HOLD / TRIM / SELL]**

**Decision Framework:**
| Price vs FMV | Recommendation |
|--------------|----------------|
| >20% below FMV | Strong Buy |
| 10-20% below | Buy |
| ±10% of FMV | Hold |
| 10-20% above | Trim |
| >20% above | Sell |

**For Current Holders:**
- Action: [Hold / Trim X% / Add / Exit]
- Target size: [% of portfolio]
- Stop level: $XXX (-XX% from current)

**For New Buyers:**
- Entry: [Buy now / Wait for $XXX / Pass]
- Target entry with margin of safety: $XXX
- Position sizing: [% of portfolio for conviction level]

**Key Catalysts:**
1. [Near-term catalyst with date]
2. [Medium-term catalyst]
3. [Risk to watch]

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FAIR MARKET VALUE: [TICKER]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Current Price: $XXX.XX
Fair Market Value: $XXX - $XXX (mid: $XXX)
Valuation: [XX% Undervalued / Fairly Valued / XX% Overvalued]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VALUATION METHODS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
P/E (XXx on $X.XX): $XXX
P/S (X.Xx on $XX): $XXX
EV/EBITDA (XXx): $XXX
Blended (weighted): $XXX

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCENARIO ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Bull (XX%): $XXX [key driver]
Base (XX%): $XXX [assumptions]
Bear (XX%): $XXX [key risk]
Prob-weighted: $XXX

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECOMMENDATION: [BUY/HOLD/SELL]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1-2 sentence rationale]

Entry: $XXX | Target: $XXX | Stop: $XXX
Risk/Reward: X.Xx

Catalysts:
• [Catalyst 1]
• [Catalyst 2]
```

## Important Guidelines

**Multiple Selection:**
- Use peer median as baseline
- Adjust for growth differential (higher growth = higher multiple)
- Adjust for margin profile (higher margins = higher multiple)
- Adjust for risk factors (higher risk = lower multiple)
- Document every adjustment

**Scenario Probabilities:**
- Sum must equal 100%
- Typical ranges: Bull 20-35%, Base 50-60%, Bear 15-25%
- Adjust based on visibility and uncertainty

**Valuation Ranges:**
- Always provide range, not point estimate
- Standard range: ±5-10% around midpoint
- Widen for high-uncertainty names

**Show Your Work:**
- Make all inputs explicit
- Document sources for estimates
- Explain multiple selection rationale
- Make reasoning transparent and auditable

See `references/valuation-methods.md` for detailed methodology.
