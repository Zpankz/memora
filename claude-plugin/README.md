# Memora Plugin for Claude Code

Persistent memory and knowledge management. Auto-injects relevant context at session start, captures significant actions (git commits, test results, research), and provides 31 memory tools via MCP.

## Installation

### From marketplace (recommended)

```bash
# Add the marketplace
/plugin marketplace add Zpankz/memora

# Install the plugin
/plugin install memora@Zpankz/memora
```

### Local development

```bash
claude --plugin-dir ./claude-plugin
```

## Prerequisites

Memora must be installed in a Python environment discoverable by the plugin:

```bash
# Option 1: pip install (recommended)
pip install git+https://github.com/Zpankz/memora

# Option 2: uv tool install
uv tool install git+https://github.com/Zpankz/memora
```

The plugin's hook runner (`scripts/run-hook.sh`) will automatically discover memora in your system Python or via `uv run`.

## What's included

| Component | Description |
|-----------|-------------|
| `.mcp.json` | Auto-registers the memora MCP server (31 tools) |
| `hooks/hooks.json` | SessionStart context injection + PostToolUse auto-capture |
| `skills/memora/` | Skill for proactive memory search and management |
| `scripts/` | Portable hook handlers with Python discovery |

## Configuration

### Environment variables

Set these in your shell or in `.mcp.json` env section:

| Variable | Default | Description |
|----------|---------|-------------|
| `MEMORA_EMBEDDING_MODEL` | `tfidf` | Embedding backend (`tfidf`, `openai`, `local`) |
| `MEMORA_AUTO_CAPTURE` | `false` | Enable PostToolUse auto-capture |
| `OPENAI_API_KEY` | — | Required only if using `openai` embeddings |
| `MEMORA_DB_PATH` | `~/.memora/memora.db` | SQLite database location |

### Overriding MCP server config

To use OpenAI embeddings or enable the graph visualization, override in your project's `.mcp.json`:

```json
{
  "mcpServers": {
    "memora": {
      "command": "memora-server",
      "args": [],
      "env": {
        "MEMORA_EMBEDDING_MODEL": "openai",
        "OPENAI_API_KEY": "sk-...",
        "MEMORA_GRAPH_PORT": "8765"
      }
    }
  }
}
```

## Plugin structure

```
claude-plugin/
├── .claude-plugin/
│   └── plugin.json        # Plugin manifest
├── .mcp.json              # MCP server configuration
├── hooks/
│   └── hooks.json         # Hook event configuration
├── scripts/
│   ├── run-hook.sh        # Portable Python discovery wrapper
│   ├── session_start.py   # SessionStart hook handler
│   └── post_tool_use.py   # PostToolUse hook handler
├── skills/
│   └── memora/
│       └── SKILL.md       # Memory management skill
└── README.md
```
