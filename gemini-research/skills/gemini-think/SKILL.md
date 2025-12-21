---
name: gemini-think
description: Deep analysis with multi-step reasoning for complex problems. Use when comparing options with tradeoffs, synthesizing information from many sources, or problems requiring explicit reasoning chains. Higher compute cost - only for genuinely complex analysis.
---

# Gemini Think

Deep reasoning for complex problems. Uses extended thinking for multi-step analysis.

## When To Use This Skill

- User asks to "compare", "analyze", "evaluate tradeoffs"
- User needs multi-step technical analysis
- Problem requires synthesizing information from many sources
- User asks "what are the implications of", "which option is better for"
- Complex decisions with multiple factors to weigh

## When NOT To Use This Skill

- Simple questions or explanations (use `gemini-ask`)
- Quick lookups or fact checks (use `gemini-search`)
- If the answer is straightforward, this wastes compute

## Command

```bash
gemini-ask think '<query>' [-i <interaction_id>]
```

**Response time:** 10-15 seconds

## Examples

```bash
# Complex comparisons
gemini-ask think 'Compare Kubernetes vs Docker Swarm for a 50-person startup'

# Multi-factor analysis
gemini-ask think 'Analyze the tradeoffs between microservices and monolith for our e-commerce platform'

# Synthesizing research
gemini-ask think 'What are the implications of recent AI regulation proposals for tech companies?'

# Follow-up with deep analysis
gemini-ask think 'Given our constraints, which approach minimizes risk?' -i abc123
```

## Stateful Conversations

Every response includes an `interaction_id`. Use `-i <id>` to continue with full context. You can switch between `gemini-ask` and `gemini-think` mid-conversation.

```bash
# Start with general question
gemini-ask ask 'What are the main cloud providers?'
# interaction_id: abc123

# Escalate to deep analysis
gemini-ask think 'Compare AWS, GCP, and Azure for ML workloads' -i abc123
```

## Options

| Option | Description |
|--------|-------------|
| `-i, --interaction <ID>` | Continue from previous interaction |
| `-f, --file <FILE>` | Include file(s) for analysis (repeatable) |
| `-o, --output <FORMAT>` | Output format: `text` (default) or `json` |

## Response Format

```
[Detailed analysis with reasoning]

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
