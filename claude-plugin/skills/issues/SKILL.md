---
name: issues
description: View and manage issue/bug memories in Memora. Use when the user says "show issues", "what bugs are open", or wants to track problems.
user-invocable: true
---

# /memora:issues — Issue Tracking

View, create, and manage issue/bug memories in Memora.

## Workflow

1. **List open issues**:
   ```
   memory_list(tags_any=["memora/issues"], metadata_filters={"status": "open"}, sort_by_importance=true)
   ```

2. **Present as a severity-sorted list**:
   - Group by severity (critical → major → minor)
   - Show: ID, content preview, severity, component, creation date
   - Flag stale items (> 14 days old)

3. **Based on arguments**:
   - `add <text>` → Create new issue: `memory_create_issue(content, severity, component)`
   - `resolve <id>` → Close issue: `memory_update(id, metadata={"status": "closed", "closed_reason": "complete"})`
   - `wontfix <id>` → Close as won't fix: `memory_update(id, metadata={"status": "closed", "closed_reason": "not_planned"})`
   - `critical`/`major`/`minor` → Filter by severity

4. **Report**: open count, by severity breakdown, stale count.

## Arguments

| Argument | Action |
|----------|--------|
| (none) | List all open issues |
| `add <text>` | Create new issue |
| `resolve <id>` | Mark as resolved |
| `wontfix <id>` | Mark as won't fix |
| `all` | Include closed issues |
| `critical` | Filter critical only |
