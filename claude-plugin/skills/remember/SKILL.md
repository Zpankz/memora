---
name: remember
description: Save a memory to Memora. Use when the user says "remember this", "save this", "store this", or wants to persist a decision, pattern, or insight for future sessions.
user-invocable: true
---

# /memora:remember — Save a Memory

Save information to Memora's persistent memory store for cross-session recall.

## Workflow

1. **Determine memory type** from context:
   - General knowledge/decision/pattern → `memory_create`
   - Task or action item → `memory_create_todo`
   - Bug or problem → `memory_create_issue`

2. **Check for duplicates** before creating:
   - Run `memory_hybrid_search` with the content summary (top_k=3, min_score=0.3)
   - If a close match exists (score > 0.7), ask the user whether to update the existing memory or create a new one

3. **Create the memory** with:
   - Clear, concise content (not raw conversation text)
   - Relevant tags (use `memora/` namespace, e.g., `memora/decisions`, `memora/patterns`, `memora/architecture`)
   - Metadata: include `project` (from cwd), `section`/`subsection` for hierarchy placement
   - For TODOs: set `priority` (high/medium/low) and `category`
   - For issues: set `severity` (critical/major/minor) and `component`

4. **Link to related memories** if appropriate:
   - Use `memory_link` with typed edges: `references`, `implements`, `supersedes`, `extends`, `contradicts`, `related_to`

5. **Confirm** the save with memory ID and a brief summary.

## Arguments

If invoked as `/memora:remember <text>`, use the provided text as the memory content. If no arguments, extract the most significant insight/decision/pattern from the recent conversation context.

## Tag Conventions

| Category | Tags |
|----------|------|
| Decisions | `memora/decisions`, `memora/architecture` |
| Patterns | `memora/patterns`, `memora/conventions` |
| Knowledge | `memora/knowledge`, `memora/reference` |
| Debugging | `memora/debugging`, `memora/gotchas` |
| Project | `memora/project/<name>` |

## Example

User: "remember that we decided to use double-dash for meta-group directories"

→ `memory_create` with:
- content: "Naming convention: double-dash (--) for meta-group directories (e.g., E2--mechanics), single-dash for leaf clusters (e.g., E2-airway-surfactant)"
- tags: ["memora/decisions", "memora/conventions", "memora/project/dual-lo-saq"]
- metadata: { "project": "dual-lo-saq", "section": "dual-lo-saq", "subsection": "conventions" }
