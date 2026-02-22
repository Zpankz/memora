---
name: status
description: Show Memora memory status dashboard. Quick overview of memory counts, open items, recent activity, and system health.
user-invocable: true
---

# /memora:status — Memory Dashboard

Show a quick status overview of the Memora memory store.

## Workflow

1. **Get statistics**:
   ```
   memory_stats()
   ```

2. **Get tag distribution**:
   ```
   memory_tags()
   ```

3. **Get open items count**:
   ```
   memory_list(tags_any=["memora/todos"], metadata_filters={"status": "open"}, limit=0)
   memory_list(tags_any=["memora/issues"], metadata_filters={"status": "open"}, limit=0)
   ```

4. **Present dashboard**:
   ```
   Memora Status
   ─────────────
   Total memories: N
   Open TODOs:     N (H high, M medium, L low)
   Open issues:    N (C critical, J major, I minor)
   Tags:           N unique
   Last created:   <date>
   Backend:        local/cloud
   ```

5. **Flag any concerns**: stale items, unlinked orphans, missing embeddings.
