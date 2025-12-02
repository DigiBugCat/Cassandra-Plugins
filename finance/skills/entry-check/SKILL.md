---
name: entry-check
description: Analyze trade entry timing and position sizing discipline. Use when discussing trade entries, position sizing, or when about to enter a new stock/options position. Prevents FOMO buying at highs and enforces staged entry discipline with zone-based sizing recommendations.
license: MIT
---

# Entry Check

Analyzes potential trade entries against price history and provides sizing guidance to prevent FOMO entries and enforce discipline.

## When This Skill Triggers

- User mentions entering a new position
- User asks about position sizing
- User discusses timing entries on any ticker
- After any discussion about buying calls/puts at current levels
- User shares a brokerage statement or trade history for review

## Workflow

### 1. Gather Price Context

For the ticker being analyzed, fetch recent price history using available market data tools:

```
Get 20-day price history for TICKER
Get current price snapshot
```

Calculate:
- **20-day high/low range**
- **Current percentile within range** (0-100)
- **Distance from 20-day high** (%)
- **Zone classification**

### 2. Zone Classification

| Zone | Percentile | Description |
|------|------------|-------------|
| **OVERBOUGHT** | >80% | Near highs, max caution |
| **UPPER_RANGE** | 60-80% | Elevated, moderate caution |
| **MID_RANGE** | 40-60% | Neutral, standard sizing |
| **LOWER_RANGE** | 20-40% | Favorable, larger entry OK |
| **OVERSOLD** | <20% | Aggressive entry warranted |

### 3. Sizing Rules by Zone

| Zone | Initial Entry % | Rationale |
|------|-----------------|-----------|
| **OVERBOUGHT** | 15-25% | Near highs, max caution |
| **UPPER_RANGE** | 25-35% | Elevated, moderate caution |
| **MID_RANGE** | 35-50% | Neutral, standard sizing |
| **LOWER_RANGE** | 50-60% | Favorable, larger OK |
| **OVERSOLD** | 60-75% | Aggressive entry warranted |

### 4. Conviction Adjustment

- **Low conviction**: Reduce sizing by 50%
- **Medium conviction**: Standard sizing
- **High conviction**: Increase sizing by 50% (capped at 60% initial)

### 5. Display Entry Analysis

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENTRY CHECK: [TICKER]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Price: $XXX.XX
Zone: [OVERBOUGHT/UPPER/MID/LOWER/OVERSOLD]
20d Percentile: XX%
Distance from 20d High: -X.X%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SIZING RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Intended: $XX,XXX
Recommended Now: $X,XXX (XX%)
Rationale: [Why this sizing]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENTRY TRANCHES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Now:  $X,XXX (XX%) @ current
2. -5%:  $X,XXX (XX%) @ $XXX.XX
3. -10%: $X,XXX (XX%) @ $XXX.XX

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WARNINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Any caution flags about timing]
```

### 6. Tranche Generation

Generate pullback tranches based on zone:

**OVERBOUGHT zone:**
- Now: 15-25%
- -5%: 25%
- -10%: 30%
- -15%: 30%

**MID_RANGE zone:**
- Now: 40%
- -5%: 30%
- -10%: 30%

**OVERSOLD zone:**
- Now: 60%
- -5%: 40%

## Key Warnings to Flag

Always warn if:
- Entry is within 5% of 20-day high
- Entry is within 2% of 52-week high
- User sizing 100% of intended position at once
- Multiple large entries in same session (FOMO pattern)
- Entry after a big run-up (>5% in prior 5 days)

## Backtest Mode

When analyzing past trades from statements:

```
BACKTEST: [DATE] Entry
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Asset: [TICKER]
Entry Price: $XXX @ [ZONE]
Tool Would Have Said: XX% initial ($X,XXX)
You Actually Did: XX% ($XX,XXX)
Outcome: [What happened next]
Lesson: [Key takeaway]
```

## Example

**User says:** "I'm thinking of buying $10K of QQQ calls here"

**Response:**
1. Fetch QQQ 20-day price data
2. Calculate current percentile (e.g., 85th = OVERBOUGHT)
3. Recommend 15-25% initial ($1,500-2,500)
4. Show tranches for remaining capital on pullbacks
5. Warn about proximity to recent highs
