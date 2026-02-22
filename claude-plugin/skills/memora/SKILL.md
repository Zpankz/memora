---
name: memora
description: Persistent memory and knowledge management. Core behavior skill that defines how to use Memora MCP tools for context injection, memory search, and knowledge capture across sessions.
user-invocable: false
---

# Memora — Persistent Memory System

Memora provides persistent memory storage with semantic search, knowledge graphs, and cross-session context. This skill defines the core behaviors for interacting with the memory store.

## Available Commands

| Command | Purpose |
|---------|---------|
| `/memora:remember` | Save a memory (decision, pattern, insight) |
| `/memora:recall` | Search and recall stored memories |
| `/memora:status` | Memory dashboard (counts, open items) |
| `/memora:todos` | View and manage TODO memories |
| `/memora:issues` | View and manage issue/bug memories |
| `/memora:insights` | Analytics, activity summary, patterns |
| `/memora:cleanup` | Find duplicates, merge, prune stale |
| `/memora:graph` | Knowledge graph export and visualization |
| `/memora:sync` | Cloud sync operations |
| `/memora:doctor` | Health check and repair |

## Session Start

At the beginning of each session, the SessionStart hook automatically searches for relevant memories based on the working directory and injects them as context. No manual action needed.

## Auto-Capture

When `MEMORA_AUTO_CAPTURE=true` is set, the PostToolUse hook automatically captures:
- Git commits (commit message provides context)
- Test results (pass/fail outcomes)
- WebFetch research (URL + content)
- Documentation edits (README, CLAUDE.md)

It does NOT capture raw code edits (they lack conversation context).

## Memory Search

When the user asks about past work, stored knowledge, or previously discussed topics:

1. Use `memory_hybrid_search` for general queries (combines keyword + semantic)
2. Use `memory_semantic_search` for conceptual/meaning-based lookups
3. Use `memory_list` with tag/date/metadata filters for structured browsing
4. Use `memory_related` to traverse the knowledge graph from a known memory

Always cite memory IDs: "Memory #42 shows..."

## Saving Memories

When the user asks to remember something, or when important decisions emerge:

1. **Check for duplicates first**: `memory_hybrid_search` with the content summary
2. **Choose the right type**:
   - General knowledge → `memory_create`
   - Task/action item → `memory_create_todo`
   - Bug/problem → `memory_create_issue`
3. **Tag consistently**: Use `memora/` namespace (e.g., `memora/decisions`, `memora/patterns`)
4. **Include metadata**: `section`, `subsection`, `project` for hierarchy placement

## Linking Related Memories

When creating or finding memories that relate to each other, use `memory_link` with typed edges:
- `references` — General reference
- `implements` — Source implements target
- `supersedes` — Source replaces target
- `extends` — Source builds upon target
- `contradicts` — Source conflicts with target
- `related_to` — Generic relationship

## Agents

- **memory-curator**: Autonomous maintenance — dedup, organize, rebuild indexes
- **memory-researcher**: Deep search and synthesis across the memory store
