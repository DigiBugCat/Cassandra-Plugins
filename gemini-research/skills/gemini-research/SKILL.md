---
name: gemini-research
description: Perform deep research using Google's Gemini Interactions API with stateful conversations, web grounding, and multi-level reasoning. Use when the user needs current information from the web, wants to research a topic thoroughly, needs fact-checked answers with sources, or requires multi-step analysis of complex questions.
---

# Gemini Research

CLI tool (`gemini-ask`) for stateful, web-grounded research using Google's Gemini Interactions API.

## When This Skill Triggers

- User asks for current/recent information not in your training data
- User wants to research a topic with web sources
- User needs fact-checked answers with citations
- User asks complex questions requiring deep analysis
- User wants to continue a previous research thread
- User says "search for", "look up", "research", "find out about"

## Commands

### search - Quick Context Gathering
```bash
gemini-ask search '<query>' [--max-results N]
gemini-ask --search '<query>'  # shorthand
```
**PURPOSE:** Fast web search for gathering context and finding sources. Minimal reasoning.

**USE WHEN:**
- Gathering background context before answering
- Finding recent news, articles, or documentation
- Quick fact checks (prices, dates, versions)
- Building a list of sources to reference

**DO NOT USE FOR:** Questions requiring explanation or analysis.

**Response time:** 3-7 seconds

### ask - General Questions (DEFAULT)
```bash
gemini-ask ask '<query>' [-i <interaction_id>]
gemini-ask --ask '<query>' [-i <interaction_id>]  # shorthand
```
**PURPOSE:** Answer general questions with web grounding. This is the default command for most queries.

**USE WHEN:**
- Answering straightforward questions
- Explaining concepts or topics
- Getting current information with context
- Most research tasks

**DO NOT USE FOR:** Multi-step analysis or comparing complex tradeoffs.

**Response time:** 8-12 seconds

### think - Complex Analysis Only
```bash
gemini-ask think '<query>' [-i <interaction_id>]
gemini-ask --think '<query>' [-i <interaction_id>]  # shorthand
```
**PURPOSE:** Deep reasoning for genuinely complex problems. Uses significantly more compute.

**USE ONLY WHEN:**
- Comparing multiple complex options with tradeoffs
- Multi-step technical analysis
- Problems requiring explicit reasoning chains
- Synthesizing information from many sources

**DO NOT USE FOR:** Simple questions, lookups, or explanations. Use `ask` instead.

**Response time:** 10-15 seconds

## Command Selection Guide

```
Is it a quick lookup or context gathering?
  → YES: use `search`
  → NO: ↓

Does it require multi-step reasoning or complex tradeoff analysis?
  → YES: use `think`
  → NO: use `ask` (default)
```

**Rule of thumb:** When in doubt, use `ask`. Only escalate to `think` for genuinely complex problems.

## Stateful Conversations with `-i`

Every response includes an `interaction_id`. Use `-i <id>` with any command to continue the conversation with full context preserved.

```bash
# Initial query
gemini-ask ask 'What are the latest AI developments?'
# Response includes: interaction_id: abc123...

# Follow-up (maintains full context)
gemini-ask ask 'Tell me more about the hardware advances' -i abc123

# Can switch reasoning depth mid-conversation
gemini-ask think 'Analyze the implications for enterprise adoption' -i abc123
```

**Key point:** The `-i` flag works on `ask` and `think` commands. No separate follow-up command needed.

## Global Options

| Option | Description |
|--------|-------------|
| `-i, --interaction <ID>` | Continue from previous interaction |
| `-f, --file <FILE>` | Include file(s) for analysis (repeatable) |
| `-o, --output <FORMAT>` | Output format: `text` (default) or `json` |

## Workflow Patterns

### Pattern 1: Quick Lookup
```bash
gemini-ask ask 'What is the current price of Bitcoin?'
```

### Pattern 2: Research Deep Dive
```bash
# Start with broad search
gemini-ask search 'renewable energy trends 2024'

# Deep analysis
gemini-ask think 'Analyze the state of solar energy adoption globally'
# Save interaction_id from response

# Follow-up on specifics
gemini-ask ask 'What about residential adoption rates?' -i <id>
```

### Pattern 3: Multi-Turn Investigation
```bash
# Initial overview
gemini-ask ask 'Explain the current state of quantum computing'
# interaction_id: abc123

# Drill into specifics (context preserved)
gemini-ask ask 'What companies are leading?' -i abc123
gemini-ask think 'Compare their technical approaches' -i abc123
gemini-ask ask 'What are the investment implications?' -i abc123
```

### Pattern 4: File Analysis
```bash
gemini-ask ask 'Summarize this document' -f report.pdf
gemini-ask think 'What are the key risks mentioned?' -f report.pdf -i <id>
```

## Response Format

All commands return:
```
[Answer text]

Sources:
1. [Source](URL)
2. [Source](URL)
...

---
To follow up, use interaction_id: <id>
Request completed in X.XXs
```

**Important:** Save the `interaction_id` from the response to use with `-i` for follow-up queries.

## Best Practices

### Default to `ask`
Most queries should use `ask`. It handles general questions, explanations, and research well.

### Reserve `think` for Complexity
Only use `think` when you need:
- Explicit multi-step reasoning
- Complex tradeoff analysis
- Synthesis across many sources

If the answer is straightforward, `think` wastes compute. Use `ask`.

### Use `search` for Context
Before answering complex questions, gather context:
```bash
gemini-ask search 'topic keywords'  # gather sources
gemini-ask ask 'actual question'    # answer with context
```

### Effective Queries
- Be specific in your questions
- Include context for better results
- Use `-i` to build on previous responses instead of repeating context

### Presenting Results
- Always include sources from the response
- Synthesize multiple queries into coherent answers
- Note when information is current vs. from training data

## Limitations

- Searches return current web content (quality varies)
- API rate limits may apply
- Conversation state persists 1 day (free) or 55 days (paid)
- Response times vary with complexity and web latency

## Setup Requirements

- `GEMINI_API_KEY` environment variable
- Get key from: https://aistudio.google.com/app/apikey
