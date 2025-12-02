---
name: format-doc
description: Format research documents with clean markdown structure, proper hierarchy, and financial formatting standards. Use when cleaning up messy notes, formatting research documents, applying consistent styling to markdown files, or preparing documents for publication.
license: MIT
---

# Format Document

Applies clean formatting and structure to research content, ensuring consistency and readability for financial research documents.

## When This Skill Triggers

- User shares messy or unformatted markdown content
- User asks to "clean up" or "format" a document
- User pastes notes that need structuring
- User wants to apply consistent styling to research
- User preparing a document for sharing or publication

## Formatting Standards

### 1. Document Structure

**Required Elements:**
- YAML frontmatter with metadata
- Single H1 title
- Clear section hierarchy (H2 → H3 → H4)
- Horizontal dividers (`---`) between major sections
- Executive summary or TL;DR at top

**Frontmatter Template:**
```yaml
---
title: [Document Title]
date: YYYY-MM-DD
tags: [tag1, tag2, tag3]
status: [Draft/Complete/Ongoing]
---
```

### 2. Text Enhancement

**Bold Usage:**
- **Bold** key terms on first mention
- **Bold** important numbers and metrics
- **Bold** conclusions and recommendations

**Italic Usage:**
- *Italics* for quotes and citations
- *Italics* for technical terms being defined
- *Italics* for emphasis within sentences

**Lists:**
- Use bullets for unordered items
- Use numbers for sequential steps or ranked items
- Nest consistently (max 2 levels deep)
- Keep list items parallel in structure

### 3. Financial Content Formatting

**Numbers and Metrics:**
- Use commas for thousands: $1,234,567
- Use consistent decimal places: 12.5% not 12.50% or 12.5000%
- Include units: $50B, 15%, 3.5x
- Use parentheses for negative: ($1.2M) or -$1.2M

**Tables:**
```markdown
| Metric | Value | Change |
|--------|-------|--------|
| Revenue | $50B | +15% |
| EPS | $2.50 | +8% |
```

**Formulas (LaTeX):**
- Inline math: `$variable$` renders as $variable$
- Block equations:
```markdown
$$
f = \frac{bp - q}{b}
$$
```

### 4. Section Templates

**For Analysis Documents:**
```markdown
# [Title]

## Executive Summary
[2-3 sentences]

---

## Key Findings
- Finding 1
- Finding 2

---

## Detailed Analysis
### [Subsection 1]
[Content]

### [Subsection 2]
[Content]

---

## Conclusion
[Summary and recommendations]

---

## Sources
1. [Source 1]
2. [Source 2]
```

**For Trade Ideas:**
```markdown
# [Ticker/Theme] Trade Idea

## TL;DR
[One sentence thesis]

---

## Thesis
[Core argument]

## Bull Case (XX%)
[Upside scenario]

## Bear Case (XX%)
[Downside scenario]

---

## Implementation
[How to execute]

## Risk Management
[Position sizing, stops]
```

### 5. Quality Checklist

Before completing, verify:
- [ ] Frontmatter includes date, title, tags
- [ ] Headers follow proper hierarchy (no skipped levels)
- [ ] Key concepts bolded on first mention
- [ ] Lists properly formatted and parallel
- [ ] Sections separated with dividers
- [ ] Quotes properly attributed
- [ ] Numbers formatted consistently
- [ ] Sources linked or referenced
- [ ] Math uses proper LaTeX syntax
- [ ] No orphaned content outside sections

## Transformation Example

**Before:**
```
Trading Strategy Analysis

The Kelly Criterion is calculated as f = (bp - q) / b where p is probability.

Important: This can lead to large drawdowns. You should use fractional kelly.
Sources: https://example.com
```

**After:**
```markdown
---
title: Trading Strategy Analysis
date: 2025-01-27
tags: [trading, kelly-criterion, risk-management]
---

# Trading Strategy Analysis

---

## Kelly Criterion

The **Kelly Criterion** is calculated as:

$$
f = \frac{bp - q}{b}
$$

where:
- $p$ = probability of winning
- $q$ = probability of losing (1 - p)
- $b$ = odds received on the wager

---

## Risk Considerations

**Important:** This can lead to large drawdowns if not used carefully.

**Best Practices:**
- Use **fractional Kelly** (typically half-Kelly) to reduce volatility
- Monitor position concentration risk
- Rebalance regularly as probabilities change

---

## Sources

1. [Kelly Criterion Overview](https://example.com)
```

## Output

Return the formatted document ready to save or paste. Note any:
- Ambiguities requiring clarification
- Missing information (dates, sources, etc.)
- Suggested additional sections
