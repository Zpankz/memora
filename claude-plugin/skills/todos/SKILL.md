---
name: todos
description: View and manage TODO memories in Memora. Use when the user says "show my todos", "what tasks are open", or wants to manage action items.
user-invocable: true
---

# /memora:todos — TODO Management

View, create, and manage TODO/task memories in Memora.

## Workflow

1. **List open TODOs**:
   ```
   memory_list(tags_any=["memora/todos"], metadata_filters={"status": "open"}, sort_by_importance=true)
   ```

2. **Present as a prioritized list**:
   - Group by priority (high → medium → low)
   - Show: ID, content preview, priority, category, creation date
   - Flag stale items (> 14 days old)

3. **Based on arguments**:
   - `add <text>` → Create new TODO: `memory_create_todo(content, priority, category)`
   - `done <id>` → Close TODO: `memory_update(id, metadata={"status": "closed", "closed_reason": "complete"})`
   - `cancel <id>` → Cancel TODO: `memory_update(id, metadata={"status": "closed", "closed_reason": "not_planned"})`
   - `high`/`medium`/`low` → Filter by priority

4. **Report**: open count, by priority breakdown, stale count.

## Arguments

| Argument | Action |
|----------|--------|
| (none) | List all open TODOs |
| `add <text>` | Create new TODO |
| `done <id>` | Mark as complete |
| `cancel <id>` | Mark as not planned |
| `all` | Include closed TODOs |
| `high` | Filter high priority only |
