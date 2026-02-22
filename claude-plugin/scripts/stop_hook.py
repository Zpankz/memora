#!/usr/bin/env python3
"""Memora Stop hook - optionally save a session summary memory.

This script:
1. Reads session info from stdin (cwd, session_id)
2. Checks if MEMORA_SESSION_SUMMARY is enabled
3. Creates a session summary memory with key context
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime


def load_memora_env():
    """Load memora environment variables from .mcp.json if available."""
    search_paths = [
        Path.cwd() / ".mcp.json",
        Path.home() / ".mcp.json",
    ]
    env_vars = {}
    for mcp_path in search_paths:
        if mcp_path.exists():
            try:
                with open(mcp_path) as f:
                    config = json.load(f)
                memora_config = config.get("mcpServers", {}).get("memora", {})
                env_vars = memora_config.get("env", {})
                for key, value in env_vars.items():
                    if key not in os.environ:
                        os.environ[key] = value
                return env_vars
            except Exception:
                pass
    return env_vars


def is_enabled(env_vars: dict) -> bool:
    """Check if session summary is enabled."""
    flag = env_vars.get(
        "MEMORA_SESSION_SUMMARY",
        os.environ.get("MEMORA_SESSION_SUMMARY", "false"),
    )
    return flag.lower() in ("true", "1", "yes")


def get_session_context(cwd: str, session_id: str) -> str:
    """Build a brief session context string."""
    project = Path(cwd).name if cwd else "unknown"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"Session ended: {project} ({timestamp})"


def save_session_marker(cwd: str, session_id: str):
    """Save a lightweight session-end marker to memora."""
    try:
        from memora import storage

        conn = storage.connect()
        project = Path(cwd).name if cwd else "unknown"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Check if there's already a session marker for this session
        results = storage.list_memories(
            conn,
            metadata_filters={
                "type": "session-marker",
                "session_id": session_id,
            },
            limit=1,
        )

        if results:
            # Update existing marker
            storage.update_memory(
                conn,
                memory_id=results[0]["id"],
                content=f"Session ended: {project} at {timestamp}",
            )
        else:
            # Create new session marker
            storage.add_memory(
                conn,
                content=f"Session ended: {project} at {timestamp}",
                metadata={
                    "type": "session-marker",
                    "session_id": session_id,
                    "project": project,
                    "cwd": cwd,
                    "ended_at": timestamp,
                },
                tags=["memora/sessions"],
            )

        conn.close()

        try:
            storage.sync_to_cloud()
        except Exception:
            pass

    except ImportError:
        pass
    except Exception:
        pass


def main():
    """Main entry point for Stop hook."""
    try:
        env_vars = load_memora_env()

        if not is_enabled(env_vars):
            print(json.dumps({}))
            sys.exit(0)

        input_data = json.load(sys.stdin)
        cwd = input_data.get("cwd", os.getcwd())
        session_id = input_data.get("session_id", "unknown")

        save_session_marker(cwd, session_id)

        context = get_session_context(cwd, session_id)
        output = {"systemMessage": f"[Memora] {context}"}
        print(json.dumps(output))

    except Exception:
        print(json.dumps({}))

    sys.exit(0)


if __name__ == "__main__":
    main()
