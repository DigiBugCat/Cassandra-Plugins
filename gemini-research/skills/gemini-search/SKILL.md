---
name: gemini-search
description: Quick web search for current information using Gemini. Use when gathering context, checking recent news, finding version numbers, prices, dates, or building a list of sources. Fast lookups only - not for explanations or analysis.
---

# Gemini Search

Fast web search for gathering context and current information. Minimal reasoning, maximum speed.

## When To Use This Skill

- User asks for recent news or current events
- User needs quick facts: prices, dates, versions, statistics
- User says "search for", "look up", "find", "what's the latest"
- You need background context before answering a complex question
- User wants a list of sources or links on a topic

## When NOT To Use This Skill

- User wants an explanation or analysis (use `gemini-ask`)
- User needs complex reasoning or comparisons (use `gemini-think`)
- User asks "why" or "how" questions that need context

## Command

```bash
gemini-ask search '<query>' [--max-results N]
```

**Response time:** 3-7 seconds

## Examples

```bash
# Current information
gemini-ask search 'Bitcoin price today'
gemini-ask search 'Node.js latest LTS version'

# Recent news
gemini-ask search 'OpenAI announcements December 2024'

# Gathering sources
gemini-ask search 'renewable energy adoption statistics 2024'
```

## Options

| Option | Description |
|--------|-------------|
| `--max-results N` | Limit number of search results |
| `-o, --output <FORMAT>` | Output format: `text` (default) or `json` |

## Response Format

```
[Search results with key information]

Sources:
1. [Source](URL)
2. [Source](URL)
...

---
Request completed in X.XXs
```

## Setup

Requires `GEMINI_API_KEY` environment variable. Get key from: https://aistudio.google.com/app/apikey
