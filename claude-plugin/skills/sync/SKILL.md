---
name: sync
description: Manage Memora cloud sync operations. Use when the user wants to sync memories to/from cloud storage (S3, R2, D1).
user-invocable: true
---

# /memora:sync — Cloud Sync

Manage cloud synchronization for Memora's memory database.

## Workflow

1. **Check sync status**:
   ```
   memory_stats()
   ```
   Report backend type, sync state, last sync timestamp.

2. **Based on arguments**:
   - `status` → Show current sync configuration and state
   - `push` → Run `memora-server sync-push` via Bash
   - `pull` → Run `memora-server sync-pull` via Bash
   - `export` → Export all memories to JSON backup: `memory_export()`
   - `import` → Import memories from JSON: `memory_import(data, strategy)`

3. **For export**, save to a timestamped file:
   ```
   memory_export() → write to ~/memora-backup-<date>.json
   ```

4. **Report results**: sync status, memory count, last sync time.

## Arguments

| Argument | Action |
|----------|--------|
| (none) | Show sync status |
| `status` | Detailed sync info |
| `push` | Force push to cloud |
| `pull` | Force pull from cloud |
| `export` | Export JSON backup |
| `import <path>` | Import from JSON file |

## Prerequisites

Cloud sync requires one of:
- `MEMORA_STORAGE_URI=s3://...` with AWS credentials
- `MEMORA_STORAGE_URI=d1://...` with Cloudflare API token
