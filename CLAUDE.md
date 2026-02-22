# Memora

## Memory System

**Memora is the persistent memory system for this project.** It provides cross-session context injection, semantic search, knowledge graphs, and structured memory management via 31 MCP tools.

All memory operations go through Memora MCP tools. Behavior is defined in the plugin skills.

## Quick Reference

### Commands

| Command | Purpose |
|---------|---------|
| `/memora:remember` | Save a memory (decision, pattern, insight) |
| `/memora:recall` | Search and recall stored memories |
| `/memora:status` | Memory dashboard |
| `/memora:todos` | Manage TODO memories |
| `/memora:issues` | Manage issue/bug memories |
| `/memora:insights` | Analytics and pattern analysis |
| `/memora:cleanup` | Deduplicate, merge, prune |
| `/memora:graph` | Knowledge graph visualization |
| `/memora:sync` | Cloud sync operations |
| `/memora:doctor` | Health check and repair |

### Agents

| Agent | Purpose |
|-------|---------|
| `memory-curator` | Autonomous memory maintenance and organization |
| `memory-researcher` | Deep search and knowledge synthesis |

### Hooks

| Hook | Trigger | Purpose |
|------|---------|---------|
| SessionStart | Session begins | Inject relevant memories as context |
| PostToolUse | After tool use | Auto-capture git commits, test results, research |
| Stop | Session ends | Save session marker (when MEMORA_SESSION_SUMMARY=true) |

### Key MCP Tools

| Tool | Use Case |
|------|----------|
| `memory_hybrid_search` | Best general search (keyword + semantic) |
| `memory_create` | Save general knowledge |
| `memory_create_todo` | Save tasks with priority |
| `memory_create_issue` | Save bugs with severity |
| `memory_link` | Create typed edges between memories |
| `memory_clusters` | Detect thematic groups |
| `memory_insights` | Activity summary and pattern analysis |

### Tag Conventions

Use the `memora/` namespace:
- `memora/decisions` — Architectural and design decisions
- `memora/patterns` — Code patterns and conventions
- `memora/knowledge` — Reference knowledge
- `memora/debugging` — Debugging insights and gotchas
- `memora/todos` — Tasks (auto-assigned by `memory_create_todo`)
- `memora/issues` — Bugs (auto-assigned by `memory_create_issue`)
- `memora/auto-capture` — Auto-captured by hooks
- `memora/sessions` — Session markers

### Environment Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `MEMORA_AUTO_CAPTURE` | Enable auto-capture hook | `false` |
| `MEMORA_SESSION_SUMMARY` | Enable session-end markers | `false` |
| `MEMORA_EMBEDDING_MODEL` | Embedding backend | `openai` |
| `MEMORA_GRAPH_PORT` | Graph visualization port | `8765` |
