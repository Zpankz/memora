---
name: recall
description: Search and recall memories from Memora. Use when the user asks "what did we decide about...", "do you remember...", "what was the pattern for...", or needs past context.
user-invocable: true
---

# /memora:recall — Search Memories

Search Memora's persistent memory store and present relevant findings.

## Workflow

1. **Parse the query** from the user's request or arguments.

2. **Search with hybrid search** (best general approach):
   ```
   memory_hybrid_search(query="<user query>", top_k=10, min_score=0.1)
   ```

3. **If hybrid returns few results**, fall back to semantic search:
   ```
   memory_semantic_search(query="<user query>", top_k=10)
   ```

4. **Present results** clearly:
   - Show memory ID, content preview, tags, and creation date
   - Group by relevance or category
   - Cite memory IDs: "Memory #42 shows..."
   - If many results, summarize the top findings

5. **Offer follow-up actions**:
   - "Want me to show the full content of any memory?"
   - "Should I search with different terms?"
   - "Want to update or link any of these?"

## Arguments

If invoked as `/memora:recall <query>`, use the provided text as the search query. If no arguments, ask the user what they want to recall.

## Search Strategy

| Scenario | Tool | Parameters |
|----------|------|------------|
| General recall | `memory_hybrid_search` | semantic_weight=0.6, top_k=10 |
| Exact keyword match | `memory_list` | query="exact phrase" |
| By tag | `memory_list` | tags_any=["memora/decisions"] |
| By date range | `memory_list` | date_from="7d" |
| Related to a memory | `memory_related` | memory_id=N |
| By importance | `memory_list` | sort_by_importance=true |

## Example

User: "/memora:recall architecture decisions"

→ `memory_hybrid_search(query="architecture decisions", top_k=10, min_score=0.1)`
→ Present: "Found 4 relevant memories:
   - Memory #12: Decided to use 2-3 children rule at every hierarchy level (memora/decisions)
   - Memory #18: SAQ→LO→subtopic is the correct hierarchy direction (memora/architecture)
   - ..."
