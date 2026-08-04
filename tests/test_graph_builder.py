from kg_lab.analytics import graph_summary, relation_distribution, top_degree_nodes
from kg_lab.builder import build_graph_from_json


def test_build_graph_from_dictionary() -> None:
    payload = {
        "name": "test_graph",
        "nodes": [
            {"id": "a", "label": "Entity A", "type": "paper"},
            {"id": "b", "label": "Entity B", "type": "topic"},
        ],
        "edges": [
            {"source": "a", "target": "b", "relation": "studies"},
        ],
    }

    graph = build_graph_from_json(payload)

    assert graph.number_of_nodes() == 2
    assert graph.number_of_edges() == 1
    assert graph.nodes["a"]["label"] == "Entity A"
    assert graph.edges["a", "b"]["relation"] == "studies"


def test_graph_analytics() -> None:
    payload = {
        "nodes": [
            {"id": "paper", "label": "Paper", "type": "paper"},
            {"id": "topic", "label": "Topic", "type": "topic"},
            {"id": "method", "label": "Method", "type": "method"},
        ],
        "edges": [
            {"source": "paper", "target": "topic", "relation": "studies"},
            {"source": "paper", "target": "method", "relation": "uses"},
        ],
    }

    graph = build_graph_from_json(payload)
    summary = graph_summary(graph)
    relations = relation_distribution(graph)
    top_nodes = top_degree_nodes(graph, limit=1)

    assert summary["nodes"] == 3
    assert summary["edges"] == 2
    assert relations == {"studies": 1, "uses": 1}
    assert top_nodes[0]["id"] == "paper"
