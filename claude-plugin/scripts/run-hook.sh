#!/usr/bin/env bash
# Portable Python runner for Memora hooks.
# Discovers a Python environment with memora installed and runs the given script.
#
# Usage: run-hook.sh <script.py> [args...]
#
# Discovery order:
#   1. System python3 with memora importable (pip install / pipx / venv)
#   2. uv run --with memora (ephemeral cached env)
#   3. Falls back to bare python3 (script handles ImportError gracefully)

set -euo pipefail

SCRIPT="$1"
shift

# Try 1: memora is already importable in system Python
if python3 -c "import memora" 2>/dev/null; then
    exec python3 "$SCRIPT" "$@"
fi

# Try 2: use uv to run with memora in a cached environment
if command -v uv &>/dev/null; then
    exec uv run --with memora python3 "$SCRIPT" "$@"
fi

# Try 3: bare python3 — the hook scripts handle ImportError gracefully
exec python3 "$SCRIPT" "$@"
