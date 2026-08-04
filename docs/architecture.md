# Architecture

Knowledge Graphs Lab is organized as a modular graph intelligence pipeline. Each layer has a clear responsibility so the project can grow from a small research prototype into a more advanced knowledge graph system.

---

## 1. Input Layer

The input layer represents sources that contain knowledge before it is structured as a graph.

Examples:

- Academic paper metadata
- Research abstracts
- Citation records
- Domain notes
- Policy documents
- System logs
- Expert annotations

The current repository uses `data/sample_research_graph.json` as a lightweight structured input file.

---

## 2. Entity Layer

The entity layer defines the graph nodes. Each node has:

- A stable `id`
- A human-readable `label`
- A semantic `type`
- Optional metadata

Example node:

```json
{
  "id": "topic_kg",
  "label": "Knowledge Graphs",
  "type": "topic"
}
```

---

## 3. Relation Layer

The relation layer defines typed edges between entities. Each edge can include evidence text and optional metadata.

Example edge:

```json
{
  "source": "paper_001",
  "target": "method_entity_linking",
  "relation": "uses",
  "evidence": "The paper applies entity linking to identify key concepts."
}
```

---

## 4. Graph Core

The graph core is currently implemented with NetworkX. The main builder is:

```text
src/kg_lab/builder.py
```

It loads JSON nodes and edges into a directed graph.

---

## 5. Analytics Layer

The analytics layer computes reusable graph statistics.

Current analytics include:

- Graph size summary
- Node type distribution
- Relation distribution
- Top degree nodes
- Shortest evidence paths

Future analytics can include:

- PageRank
- Betweenness centrality
- Community detection
- Similarity search
- Link prediction
- Graph embeddings

---

## 6. Reasoning Layer

The reasoning layer is planned for explainable graph-based intelligence. It will connect user questions to evidence paths inside the graph.

A future reasoning path may look like:

```text
Question → Topic → Paper → Method → Finding → Limitation → Research Gap
```

---

## 7. Visualization Layer

The repository currently includes SVG concept previews under `assets/`. Future versions can add interactive graph visualization with a web dashboard.

Suggested visualization stack:

- React Flow for graph exploration
- D3.js for custom graph layouts
- FastAPI for backend services
- SQLite or PostgreSQL for persistence

---

## Design Goals

- Keep graph construction simple and transparent.
- Keep analytics functions small and testable.
- Preserve evidence whenever relations are created.
- Separate graph modeling from visualization.
- Make the project useful for academic research workflows.
