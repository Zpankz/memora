---
name: cleanup
description: Find and merge duplicate memories, prune stale items, and maintain memory health. Use when the user says "clean up memories", "find duplicates", or "prune stale".
user-invocable: true
---

# /memora:cleanup — Memory Maintenance

Find duplicates, merge similar memories, and prune stale items.

## Workflow

1. **Find duplicates**:
   ```
   memory_find_duplicates(min_similarity=0.7, max_similarity=0.95, limit=10, use_llm=false)
   ```
   Set `use_llm=true` only if the user wants AI-powered comparison.

2. **Present duplicate pairs** with:
   - Both memory previews
   - Similarity score
   - Suggested action (merge/keep_both/review)

3. **For each pair the user approves**, merge:
   ```
   memory_merge(source_id=<lower_quality>, target_id=<higher_quality>, merge_strategy="append")
   ```

4. **Find stale items**:
   ```
   memory_insights(period="30d", include_llm_analysis=false)
   ```
   Report open TODOs and issues that haven't been touched in 14+ days.

5. **Rebuild indexes if needed**:
   - After significant merges: `memory_rebuild_crossrefs()`
   - After embedding model change: `memory_rebuild_embeddings()`

6. **Report summary**: duplicates merged, stale items flagged, total memories before/after.

## Arguments

| Argument | Action |
|----------|--------|
| (none) | Find duplicates + stale items |
| `duplicates` | Only find duplicates |
| `stale` | Only find stale items |
| `rebuild` | Rebuild embeddings and crossrefs |
| `deep` | Use LLM for duplicate comparison |

## Safety

- Always present duplicate pairs for user approval before merging
- Never auto-delete memories without confirmation
- Show before/after counts
