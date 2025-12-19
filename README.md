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

### gemini-research

Stateful AI research using Google's Gemini Interactions API with web grounding and multi-level reasoning.

**Dependencies:**
- [gemini-ask](https://github.com/DigiBugCat/gemini-interactions-mcp) - `cargo install --git https://github.com/DigiBugCat/gemini-interactions-mcp`
- [Gemini API Key](https://aistudio.google.com/app/apikey) - Set `GEMINI_API_KEY` environment variable

**Commands:**
| Command | Description |
|---------|-------------|
| **search** | Quick web search with structured results (3-7s) |
| **ask** | Grounded answers with balanced reasoning (8-12s) |
| **think** | Deep reasoning for complex problems (10-15s) |

All commands support `-i <interaction_id>` to continue previous conversations with full context.

**Usage:**
```bash
# Quick search
gemini-ask search 'latest AI news'

# Grounded answer
gemini-ask ask 'What are the current trends in renewable energy?'

# Deep analysis
gemini-ask think 'Analyze the implications of recent Fed policy changes'

# Follow-up (use -i with any command)
gemini-ask ask 'Tell me more about inflation impact' -i <interaction_id>
```

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
