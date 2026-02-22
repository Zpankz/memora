---
name: insights
description: Get analytics and insights from Memora. Shows activity summaries, open items, stale memories, and pattern analysis. Use when the user wants a memory health check or overview.
user-invocable: true
---

# /memora:insights — Memory Analytics

Analyze stored memories and surface actionable insights.

## Workflow

1. **Run insights analysis**:
   ```
   memory_insights(period="7d", include_llm_analysis=false)
   ```
   Use `include_llm_analysis=true` only if the user explicitly requests AI-powered pattern detection (requires OpenAI API key).

2. **Get statistics**:
   ```
   memory_stats()
   ```

3. **Present a dashboard**:
   - Total memories, by type (knowledge, todos, issues, sections)
   - Recent activity (created in last 7 days)
   - Open TODOs by priority
   - Open issues by severity
   - Stale items (untouched > 14 days)
   - Tag distribution
   - Consolidation candidates (similar memories to merge)

4. **Offer actions**:
   - "Want me to clean up duplicate memories?"
   - "Should I resolve any stale TODOs?"
   - "Want deeper AI-powered pattern analysis?"

## Arguments

| Argument | Action |
|----------|--------|
| (none) | 7-day summary without LLM |
| `deep` | Full analysis with LLM patterns |
| `30d` / `1m` | 30-day analysis period |
| `todos` | Focus on open TODOs |
| `issues` | Focus on open issues |
