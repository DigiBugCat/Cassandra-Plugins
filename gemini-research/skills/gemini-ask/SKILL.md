---
name: gemini-ask
description: Answer questions using current web information with sources. Use for general research, explanations, and getting up-to-date information. This is the default for most research queries that need more than a quick lookup.
---

# Gemini Ask

Answer questions with web-grounded information. The default choice for most research tasks.

## When To Use This Skill

- User asks "what is", "how does", "explain", "tell me about"
- User needs current information with context and explanation
- User wants to understand a topic, concept, or technology
- User asks straightforward questions about any subject
- Most research tasks that aren't pure lookups

## When NOT To Use This Skill

- User just needs quick facts or current prices/versions (use `gemini-search`)
- User needs complex multi-step analysis or tradeoff comparisons (use `gemini-think`)

## Command

```bash
gemini-ask ask '<query>' [-i <interaction_id>]
```

**Response time:** 8-12 seconds

## Examples

```bash
# General questions
gemini-ask ask 'What is the current state of quantum computing?'
gemini-ask ask 'Explain how WebAssembly works'

# Current information with context
gemini-ask ask 'What are the new features in Python 3.13?'

# Follow-up on previous query
gemini-ask ask 'What about performance improvements?' -i abc123
```

## Stateful Conversations

Every response includes an `interaction_id`. Use `-i <id>` to continue the conversation with full context preserved.

```bash
# Initial query
gemini-ask ask 'What are the main AI frameworks in 2024?'
# Response includes: interaction_id: abc123

# Follow-up (context preserved)
gemini-ask ask 'Compare PyTorch and JAX specifically' -i abc123
```

## Options

| Option | Description |
|--------|-------------|
| `-i, --interaction <ID>` | Continue from previous interaction |
| `-f, --file <FILE>` | Include file(s) for analysis (repeatable) |
| `-o, --output <FORMAT>` | Output format: `text` (default) or `json` |

## Response Format

```
[Detailed answer with context]

Sources:
1. [Source](URL)
2. [Source](URL)
...

---
To follow up, use interaction_id: <id>
Request completed in X.XXs
```

## Setup

Requires `GEMINI_API_KEY` environment variable. Get key from: https://aistudio.google.com/app/apikey
