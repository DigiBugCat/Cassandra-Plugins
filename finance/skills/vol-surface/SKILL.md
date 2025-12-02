---
name: vol-surface
description: Analyze options volatility surface including term structure, skew, IV percentile/rank, and event-driven vol. Use when analyzing options for any ticker, evaluating diagonal/calendar spreads, assessing event risk, or understanding vol regime. Critical for options trading decisions.
license: MIT
---

# Volatility Surface Analysis

Analyzes options market volatility surface to identify trading opportunities, assess risk, and inform strategy selection.

## When This Skill Triggers

- User asks about options for a ticker
- User mentions volatility, IV, or term structure
- User considering options strategies (diagonals, calendars, spreads)
- User asks about event risk (earnings, FOMC)
- User wants to understand vol regime for a name

## Core Concepts

### Term Structure
The relationship between implied volatility and time to expiration.

| Pattern | Description | Implication |
|---------|-------------|-------------|
| **Contango** | Near-term IV < far-term IV | Normal market, time premium |
| **Backwardation** | Near-term IV > far-term IV | Event risk, fear |
| **Flat** | Similar IV across expirations | Uncertainty, transition |

### Skew
The relationship between implied volatility and strike price.

| Pattern | Description | Implication |
|---------|-------------|-------------|
| **Put Skew** | OTM puts > ATM > OTM calls | Normal equity skew, downside fear |
| **Call Skew** | OTM calls > ATM > OTM puts | Upside speculation, squeeze risk |
| **Smile** | Both OTM puts and calls elevated | High tail risk, binary event |

### IV Metrics

**IV Rank (0-100):**
- Where current IV sits in 52-week range
- 0 = 52-week low, 100 = 52-week high
- >50 = elevated, <50 = suppressed

**IV Percentile (0-100):**
- % of days IV was lower than current
- 90th percentile = IV higher than 90% of days
- Better for understanding distribution

## Workflow

### 1. Gather Vol Data

For the target ticker, collect:

```
Current IV:
- ATM IV (30-day)
- ATM IV by expiration (weekly, monthly, quarterly)
- 25-delta put IV
- 25-delta call IV

Historical Context:
- 52-week IV high/low
- 30-day historical volatility (HV)
- IV percentile/rank

Events:
- Next earnings date
- Days to earnings
- Other catalysts (FOMC, product launch, etc.)
```

### 2. Analyze Term Structure

Calculate slope between key expirations:

```
Term Structure Analysis:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Expiry    | Days | ATM IV | vs Front
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Date]    | XX   | XX.X%  | —
[Date]    | XX   | XX.X%  | +X.X%
[Date]    | XX   | XX.X%  | +X.X%

Slope: [Contango/Backwardation] (+/-X.X% per 30 days)
```

**Interpretation:**
- Steep contango (>2%/month): Calendar spreads attractive
- Backwardation: Event risk priced in, post-event vol crush expected
- Flat: Limited term structure edge

### 3. Analyze Skew

Measure put-call differential:

```
Skew Analysis:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Strike      | IV    | vs ATM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
25Δ Put     | XX.X% | +X.X%
ATM         | XX.X% | —
25Δ Call    | XX.X% | +/-X.X%

Put Skew Premium: +X.X%
Pattern: [Normal/Elevated Put Skew/Call Skew/Smile]
```

**Interpretation:**
- Elevated put skew (>5%): Downside protection expensive
- Flat skew: Balanced sentiment
- Call skew: Unusual, indicates squeeze or speculative demand

### 4. Context Assessment

Compare to history:

```
IV Context:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Current ATM IV:    XX.X%
52-Week High:      XX.X%
52-Week Low:       XX.X%
IV Rank:           XX/100
IV Percentile:     XXth

30-Day HV:         XX.X%
IV Premium:        +/-X.X% (IV vs HV)
```

**Interpretation:**
- IV Rank >70: Vol elevated, favor selling premium
- IV Rank <30: Vol suppressed, favor buying premium
- IV > HV: Options "expensive" vs realized
- IV < HV: Options "cheap" vs realized

### 5. Event Calendar

Note upcoming catalysts:

```
Events Affecting Vol:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Date       | Event        | Impact
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Date]     | Earnings     | High
[Date]     | FOMC         | Medium
[Date]     | OpEx         | Low
```

### 6. Strategy Implications

Based on analysis, suggest approaches:

**If Steep Contango + High IV Rank:**
- Calendar spreads (sell front, buy back)
- Diagonal spreads (directional with vol edge)

**If Backwardation (Event):**
- Post-earnings vol crush plays
- Avoid long premium through event unless directional conviction

**If Low IV Rank:**
- Long premium strategies (straddles, strangles)
- Avoid selling premium (limited edge)

**If Elevated Put Skew:**
- Put spreads more attractive than naked puts
- Consider put ratio spreads if bullish

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOL SURFACE: [TICKER]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Price: $XXX.XX
Date: YYYY-MM-DD

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TERM STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
30d: XX.X%  |  60d: XX.X%  |  90d: XX.X%
Slope: [Contango/Backwardation] (+/-X.X%)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SKEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
25Δ Put: XX.X%  |  ATM: XX.X%  |  25Δ Call: XX.X%
Put Skew: +X.X% [Normal/Elevated/Suppressed]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IV CONTEXT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IV Rank: XX/100  |  IV Percentile: XXth
30d HV: XX.X%   |  IV Premium: +/-X.X%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EVENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• [Date]: [Event] (XX days)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Vol Regime: [Low/Normal/Elevated/Extreme]
Edge: [Sell premium / Buy premium / Neutral]
Opportunity: [Brief strategy suggestion]
Risk: [Key warning if any]
```

## Strategy Selection Guide

| Term Structure | IV Rank | Recommended |
|---------------|---------|-------------|
| Contango | High (>70) | Calendars, short front-month |
| Contango | Low (<30) | Long back-month, diagonals |
| Backwardation | High | Post-event plays, avoid pre-event |
| Backwardation | Low | Rare - investigate cause |
| Flat | High | Iron condors, strangles |
| Flat | Low | Long straddles if expecting move |

## Important Guidelines

**Always Consider:**
- Events within the option expiration window
- Liquidity (bid-ask spreads)
- Earnings date relative to expiration
- Sector/market vol context

**Red Flags:**
- Extreme backwardation without known event
- IV Rank >90 (reversion likely)
- Very wide skew (tail risk priced in)
- Low liquidity in desired strikes

**Integration:**
- After vol analysis, consider position sizing
- Use entry-check skill for timing
- Document thesis before trading
