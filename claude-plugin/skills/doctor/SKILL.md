---
name: doctor
description: Diagnose and repair Memora health. Check for missing embeddings, broken links, orphaned memories, and rebuild indexes. Use when memories seem inconsistent or search isn't working well.
user-invocable: true
---

# /memora:doctor — Health Check & Repair

Diagnose and repair the Memora memory store.

## Workflow

1. **Check memory statistics**:
   ```
   memory_stats()
   ```

2. **Validate tags**:
   ```
   memory_validate_tags(include_memories=true)
   ```
   Report invalid tags that don't match the allowlist.

3. **Find duplicates** (quick scan):
   ```
   memory_find_duplicates(min_similarity=0.85, limit=5, use_llm=false)
   ```

4. **Check for orphans** — memories with no tags, no links, no hierarchy:
   ```
   memory_list(tags_none=["memora/todos", "memora/issues", "memora/knowledge", "memora/sections", "memora/decisions", "memora/auto-capture"], limit=20)
   ```

5. **Present health report**:
   ```
   Memora Health
   ─────────────
   Total memories:    N
   With embeddings:   N/N
   Duplicate pairs:   N
   Invalid tags:      N
   Orphan memories:   N
   ─────────────
   Status: HEALTHY / NEEDS ATTENTION
   ```

6. **Offer repairs**:
   - "Rebuild embeddings?" → `memory_rebuild_embeddings()`
   - "Rebuild cross-references?" → `memory_rebuild_crossrefs()`
   - "Merge duplicates?" → Guide through `/memora:cleanup`
   - "Tag orphans?" → Suggest tags for untagged memories

## Arguments

| Argument | Action |
|----------|--------|
| (none) | Full health check |
| `rebuild` | Rebuild all indexes |
| `tags` | Validate tags only |
| `fix` | Auto-fix what's safe to fix |
