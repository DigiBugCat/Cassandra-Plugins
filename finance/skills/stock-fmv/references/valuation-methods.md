# Valuation Methods Reference

Detailed methodology for multi-method stock valuation.

## Price-to-Earnings (P/E)

### Formula
```
Fair Value = EPS × P/E Multiple
```

### When to Use
- Profitable companies with stable earnings
- Mature businesses with predictable growth
- Companies with comparable peers

### Multiple Selection

**Base Multiple Sources:**
- Peer group median P/E
- Historical average P/E
- Sector average P/E

**Adjustment Factors:**

| Factor | Impact on Multiple |
|--------|-------------------|
| Higher growth vs peers | +10-30% |
| Lower growth vs peers | -10-30% |
| Higher margins | +5-15% |
| Lower margins | -5-15% |
| Higher volatility/risk | -10-20% |
| Market leader position | +10-20% |
| Cyclical business | -10-20% |

### Common Mistakes
- Using trailing P/E instead of forward
- Not adjusting for one-time items
- Ignoring differences in accounting
- Applying tech multiples to industrials

---

## Price-to-Sales (P/S)

### Formula
```
Fair Value = Revenue per Share × P/S Multiple
```

### When to Use
- High-growth companies not yet profitable
- Companies with negative or volatile earnings
- SaaS and subscription businesses
- Turnaround situations

### Multiple Selection

**Profitability Adjustment:**
```
Adjusted P/S = Peer P/S × (Company Gross Margin / Peer Gross Margin)
```

| Gross Margin | Typical P/S Range |
|--------------|-------------------|
| >70% (SaaS) | 5x - 15x |
| 50-70% | 3x - 8x |
| 30-50% | 1x - 4x |
| <30% | 0.5x - 2x |

### Common Mistakes
- Ignoring profitability differences
- Not considering path to profitability
- Using P/S for low-margin commodity businesses

---

## EV/EBITDA

### Formula
```
Enterprise Value = EBITDA × EV/EBITDA Multiple
Equity Value = Enterprise Value - Net Debt
Fair Value per Share = Equity Value / Shares Outstanding
```

### When to Use
- Capital-intensive businesses
- Companies with significant debt
- M&A analysis
- Cross-border comparisons (removes tax differences)

### Multiple Selection

| Sector | Typical EV/EBITDA |
|--------|-------------------|
| Tech/Software | 15x - 25x |
| Healthcare | 12x - 18x |
| Industrials | 8x - 12x |
| Utilities | 8x - 12x |
| Retail | 6x - 10x |
| Energy | 4x - 8x |

### Net Debt Calculation
```
Net Debt = Total Debt - Cash & Equivalents

If Net Debt is negative (net cash):
- Adds to equity value
- Company has excess cash on balance sheet
```

### Common Mistakes
- Forgetting to subtract net debt
- Using EBITDA when capex is significant
- Not adjusting for leases (IFRS 16)

---

## Scenario Analysis Framework

### Probability Assignment

**High Visibility (Stable Business):**
- Bull: 25-30%
- Base: 55-60%
- Bear: 15-20%

**Medium Visibility:**
- Bull: 20-25%
- Base: 50-55%
- Bear: 20-25%

**Low Visibility (High Uncertainty):**
- Bull: 15-20%
- Base: 45-50%
- Bear: 30-35%

### Scenario Construction

**Bull Case Drivers:**
- Revenue acceleration
- Margin expansion
- Multiple expansion
- M&A optionality
- New product success

**Bear Case Drivers:**
- Competitive pressure
- Margin compression
- Multiple contraction
- Regulatory risk
- Execution failure

### Calculating Expected Value
```
Expected FMV = Σ (Scenario FMV × Probability)

Example:
Bull ($150, 25%) + Base ($120, 55%) + Bear ($80, 20%)
= $37.50 + $66.00 + $16.00
= $119.50
```

---

## Decision Framework

### Buy/Sell Thresholds

| Price vs FMV | Action | Rationale |
|--------------|--------|-----------|
| >25% below | Strong Buy | Significant margin of safety |
| 15-25% below | Buy | Attractive entry |
| 5-15% below | Accumulate | Slight discount |
| ±5% | Hold | Fairly valued |
| 5-15% above | Trim | Slight premium |
| 15-25% above | Reduce | Expensive |
| >25% above | Sell | Significantly overvalued |

### Position Sizing by Conviction

| Conviction | Discount to FMV | Position Size |
|------------|-----------------|---------------|
| High | 0-10% | 3-5% portfolio |
| Medium | 10-20% | 2-3% portfolio |
| Low | >20% required | 1-2% portfolio |

### Risk/Reward Calculation
```
Upside = (Bull Case FMV - Current Price) / Current Price
Downside = (Current Price - Bear Case FMV) / Current Price
Risk/Reward = Upside / Downside

Target: >2:1 for new positions
```

---

## Data Sources

**Earnings Estimates:**
- Company guidance (most authoritative)
- Analyst consensus (Bloomberg, FactSet)
- Recent research reports

**Peer Multiples:**
- Bloomberg COMP function
- FactSet
- Manual peer analysis

**Historical Data:**
- 5-year historical range
- Through-cycle average
- Adjust for structural changes

---

## Quality Checks

Before finalizing valuation:

- [ ] All three methods produce reasonable results
- [ ] Blended FMV within historical valuation range
- [ ] Scenario probabilities sum to 100%
- [ ] Multiple selection documented and justified
- [ ] Net debt/cash correctly applied
- [ ] Share count current (check for buybacks/dilution)
- [ ] Estimates from recent sources (<30 days)
- [ ] Major risks reflected in bear case
