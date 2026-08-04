"""Build and inspect the sample research knowledge graph.

Run from the repository root:

    python examples/build_demo_graph.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from kg_lab.analytics import graph_summary, relation_distribution, top_degree_nodes
from kg_lab.builder import build_graph_from_json


def main() -> None:
    graph_path = ROOT / "data" / "sample_research_graph.json"
    graph = build_graph_from_json(graph_path)

    print("\nKnowledge Graph Summary")
    print(json.dumps(graph_summary(graph), indent=2))

    print("\nRelation Distribution")
    print(json.dumps(relation_distribution(graph), indent=2))

    print("\nTop Central Nodes")
    print(json.dumps(top_degree_nodes(graph, limit=5), indent=2))


if __name__ == "__main__":
    main()
