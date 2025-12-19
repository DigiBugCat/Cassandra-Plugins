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

### search - Quick Web Search
```bash
gemini-ask search '<query>' [--max-results N]
gemini-ask --search '<query>'  # shorthand
```
Fast search with minimal thinking. Returns structured results with titles, URLs, and snippets.

**Use for:**
- Finding sources before deeper analysis
- Quick fact lookups
- Gathering URLs for follow-up questions

**Response time:** 3-7 seconds

### ask - Balanced Grounded Answers
```bash
gemini-ask ask '<query>' [-i <interaction_id>]
gemini-ask --ask '<query>' [-i <interaction_id>]  # shorthand
```
Medium-depth reasoning with automatic web grounding. Model decides when to search.

**Use for:**
- General research questions
- Topics needing current information
- Questions with straightforward answers

**Response time:** 8-12 seconds

### think - Deep Reasoning
```bash
gemini-ask think '<query>' [-i <interaction_id>]
gemini-ask --think '<query>' [-i <interaction_id>]  # shorthand
```
High-level thinking for complex problems. Multi-step analysis with thorough sourcing.

**Use for:**
- Complex technical questions
- Multi-faceted analysis
- Problems requiring step-by-step reasoning
- Controversial topics needing balanced views

**Response time:** 10-15 seconds

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

### Choose the Right Command
| Need | Command |
|------|---------|
| Quick facts, find sources | `search` |
| General questions | `ask` |
| Complex analysis | `think` |
| Continue conversation | any command + `-i` |

### Effective Queries
- Be specific in your questions
- Include context for better results
- Use `-i` to build on previous responses instead of repeating context

### Managing Conversations
- Save `interaction_id` when you'll need follow-ups
- Any command can continue a conversation with `-i`
- Switch between `ask` and `think` based on complexity

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
