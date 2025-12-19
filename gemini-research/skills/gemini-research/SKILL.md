---
name: gemini-research
description: Perform deep research using Google's Gemini Interactions API with stateful conversations, web grounding, and multi-level reasoning. Use when the user needs current information from the web, wants to research a topic thoroughly, needs fact-checked answers with sources, or requires multi-step analysis of complex questions.
---

# Gemini Research

Leverages Google's Gemini Interactions API for stateful, web-grounded research with configurable reasoning depths.

## When This Skill Triggers

- User asks for current/recent information not in your training data
- User wants to research a topic with web sources
- User needs fact-checked answers with citations
- User asks complex questions requiring deep analysis
- User wants to continue a previous research thread
- User says "search for", "look up", "research", "find out about"

## MCP Tools Available

The `gemini-research` MCP server provides four tools:

### 1. `search` - Quick Web Search
```
mcp__gemini-research__search(query, max_results=10)
```
Fast search with minimal thinking. Returns structured results with titles, URLs, and snippets.

**Use for:**
- Finding sources before deeper analysis
- Quick fact lookups
- Gathering URLs for follow-up questions

**Response time:** 3-7 seconds

### 2. `ask` - Balanced Grounded Answers
```
mcp__gemini-research__ask(query, interaction_id=None, max_tokens=8192)
```
Medium-depth reasoning with automatic web grounding. Model decides when to search.

**Use for:**
- General research questions
- Topics needing current information
- Questions with straightforward answers

**Response time:** 8-12 seconds

### 3. `ask_thinking` - Deep Reasoning
```
mcp__gemini-research__ask_thinking(query, interaction_id=None, max_tokens=16384)
```
High-level thinking for complex problems. Multi-step analysis with thorough sourcing.

**Use for:**
- Complex technical questions
- Multi-faceted analysis
- Problems requiring step-by-step reasoning
- Controversial topics needing balanced views

**Response time:** 10-15 seconds

### 4. `follow_up` - Continue Conversation
```
mcp__gemini-research__follow_up(query, interaction_id, thinking_level="medium")
```
Continue a previous conversation with full context. No need to repeat prior information.

**Use for:**
- Drilling deeper into a topic
- Asking clarifying questions
- Building on previous research

**Thinking levels:** minimal, low, medium, high

## Workflow Patterns

### Pattern 1: Quick Lookup
For simple factual questions:
```
1. Use `ask` with the question
2. Present answer with sources
```

### Pattern 2: Research Deep Dive
For comprehensive research:
```
1. Use `search` to find initial sources
2. Use `ask_thinking` for in-depth analysis
3. Save the interaction_id from response
4. Use `follow_up` to explore specific aspects
5. Synthesize findings for user
```

### Pattern 3: Multi-Turn Investigation
For complex topics requiring exploration:
```
1. Start with `ask` for initial overview
2. Note the interaction_id in response
3. Use `follow_up` with that ID to explore subtopics
4. Continue follow_ups to build comprehensive understanding
5. Each follow_up maintains full conversation context
```

### Pattern 3: Comparative Analysis
For comparing options or viewpoints:
```
1. Use `ask_thinking` for the main comparison
2. Use `follow_up` to dig into specific differences
3. Request balanced pros/cons with citations
```

## Response Format

All tools return responses with:

```
[Answer text with inline citations]

Sources:
1. [Title](URL)
2. [Title](URL)
...

---
interaction_id: [ID for follow-ups]
tokens: X in, Y out, Z reasoning
```

**Important:** Always preserve and reference the `interaction_id` when doing follow-up queries.

## Best Practices

### Choose the Right Tool
| Need | Tool |
|------|------|
| Quick facts | `search` |
| General questions | `ask` |
| Complex analysis | `ask_thinking` |
| Continue research | `follow_up` |

### Effective Queries
- Be specific in your questions
- Include context for better results
- For `follow_up`, reference what you want to explore from the previous response

### Managing Conversations
- Store interaction_id when you'll need follow-ups
- Use `follow_up` to avoid re-searching same context
- Adjust thinking_level based on complexity

### Presenting Results
- Always include sources from the response
- Synthesize multiple tool calls into coherent answers
- Note when information is current vs. from training data

## Example Usage

**User:** "What are the latest developments in quantum computing?"

**Workflow:**
1. Call `ask_thinking` for comprehensive current overview
2. Present findings with sources
3. Offer to `follow_up` on specific areas (hardware, algorithms, companies)

**User:** "Tell me more about the hardware advances"

**Workflow:**
1. Use `follow_up` with saved interaction_id
2. Set thinking_level="medium" for focused depth
3. Present hardware-specific findings

## Limitations

- Searches return current web content (quality varies)
- API rate limits may apply
- Conversation state persists 1 day (free) or 55 days (paid)
- Response times vary with complexity and web latency

## Setup Requirements

The MCP server requires:
- `GEMINI_API_KEY` environment variable
- Get key from: https://aistudio.google.com/app/apikey
