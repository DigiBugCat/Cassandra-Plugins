# Cassandra Plugins

Personal Claude Code plugin marketplace.

## Installation

```bash
/plugin marketplace add DigiBugCat/Cassandra-Plugins
```

## Plugins

### yt-cli

Download and transcribe YouTube videos with speaker diarization and auto-chapters.

**Dependencies:**
- [yt-cli](https://github.com/DigiBugCat/yt-cli) - `cargo install --git https://github.com/DigiBugCat/yt-cli`
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - `brew install yt-dlp`
- [AssemblyAI API key](https://www.assemblyai.com/) - `yt-cli init -k <your-key>`

---

### finance

Financial analysis, valuation, options trading, and trade discipline skills.

**Skills included:**

| Skill | Description |
|-------|-------------|
| **entry-check** | Trade entry timing and position sizing. Prevents FOMO buying at highs with zone-based sizing and staged entry tranches. |
| **stock-fmv** | Fair market value using P/E, P/S, and EV/EBITDA methods with scenario analysis and probability weighting. |
| **vol-surface** | Options volatility surface analysis including term structure, skew, IV percentile, and event risk. |
| **format-doc** | Research document formatting with clean markdown structure and financial formatting standards. |

**Usage:**

Skills trigger automatically based on context:

```
"I'm thinking of buying $10K of NVDA here"
→ entry-check: shows zone, sizing recommendation, tranches

"What's the fair value of AAPL?"
→ stock-fmv: multi-method valuation with scenarios

"How's the vol surface looking for SPY?"
→ vol-surface: term structure, skew, IV context

"Clean up these notes"
→ format-doc: applies formatting standards
```
