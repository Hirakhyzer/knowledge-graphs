"""Graph analytics helpers for research knowledge graphs."""

from __future__ import annotations

from collections import Counter
from typing import Any

import networkx as nx


def graph_summary(graph: nx.DiGraph) -> dict[str, Any]:
    """Return a compact summary of graph size and node types."""

    node_types = Counter(data.get("type", "entity") for _, data in graph.nodes(data=True))

    return {
        "name": graph.graph.get("name", "knowledge_graph"),
        "nodes": graph.number_of_nodes(),
        "edges": graph.number_of_edges(),
        "node_types": dict(sorted(node_types.items())),
    }


def relation_distribution(graph: nx.DiGraph) -> dict[str, int]:
    """Count edge relation types in the graph."""

    relations = Counter(data.get("relation", "related_to") for _, _, data in graph.edges(data=True))
    return dict(sorted(relations.items()))


def top_degree_nodes(graph: nx.DiGraph, limit: int = 5) -> list[dict[str, Any]]:
    """Return nodes with the highest total degree."""

    ranked_nodes = sorted(graph.degree, key=lambda item: item[1], reverse=True)[:limit]

    return [
        {
            "id": node_id,
            "label": graph.nodes[node_id].get("label", node_id),
            "type": graph.nodes[node_id].get("type", "entity"),
            "degree": degree,
        }
        for node_id, degree in ranked_nodes
    ]


def shortest_evidence_path(graph: nx.DiGraph, source: str, target: str) -> list[str]:
    """Return the shortest path between two nodes when one exists."""

    return nx.shortest_path(graph, source=source, target=target)
