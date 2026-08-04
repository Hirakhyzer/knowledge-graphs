"""Utilities for building NetworkX knowledge graphs from JSON data."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import networkx as nx


GraphInput = str | Path | dict[str, Any]


def _load_payload(source: GraphInput) -> dict[str, Any]:
    if isinstance(source, dict):
        return source

    path = Path(source)
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_graph_from_json(source: GraphInput) -> nx.DiGraph:
    """Build a directed knowledge graph from a JSON file or dictionary.

    The expected structure is:

    {
      "nodes": [{"id": "p1", "label": "Paper", "type": "paper"}],
      "edges": [{"source": "p1", "target": "t1", "relation": "studies"}]
    }
    """

    payload = _load_payload(source)
    graph = nx.DiGraph(name=payload.get("name", "knowledge_graph"))

    for node in payload.get("nodes", []):
        node_id = node["id"]
        graph.add_node(
            node_id,
            label=node.get("label", node_id),
            type=node.get("type", "entity"),
            metadata=node.get("metadata", {}),
        )

    for edge in payload.get("edges", []):
        graph.add_edge(
            edge["source"],
            edge["target"],
            relation=edge.get("relation", "related_to"),
            evidence=edge.get("evidence"),
            weight=float(edge.get("weight", 1.0)),
            metadata=edge.get("metadata", {}),
        )

    return graph
