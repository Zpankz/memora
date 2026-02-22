---
name: graph
description: Export and view the Memora knowledge graph. Use when the user wants to visualize memory connections, export the graph, or open the graph UI.
user-invocable: true
---

# /memora:graph — Knowledge Graph

Export or view the Memora knowledge graph visualization.

## Workflow

1. **Check if the graph server is running** (default port 8765):
   - If `MEMORA_GRAPH_PORT` is configured, mention: "Graph UI available at http://localhost:<port>/graph"

2. **Export options** — ask the user or infer from context:
   - **View live graph**: Direct to `http://localhost:8765/graph`
   - **Export static HTML**: Use `memory_export_graph`
   - **Show cluster analysis**: Use `memory_clusters`

3. **For export**:
   ```
   memory_export_graph(output_path="~/memories_graph.html", min_score=0.25)
   ```

4. **For cluster analysis**:
   ```
   memory_clusters(min_cluster_size=2, min_score=0.3, algorithm="louvain")
   ```
   Present clusters with their common themes and member counts.

5. **Report results**: node count, edge count, cluster count, and how to access.

## Arguments

| Argument | Action |
|----------|--------|
| (none) | Show graph access info + offer export |
| `export` | Export to static HTML |
| `clusters` | Run cluster detection |
| `stats` | Show graph statistics |
