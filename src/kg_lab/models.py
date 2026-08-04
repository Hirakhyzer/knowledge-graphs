"""Typed data models for knowledge graph nodes and edges."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class KnowledgeNode:
    """A typed entity in the knowledge graph."""

    id: str
    label: str
    type: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class KnowledgeEdge:
    """A typed relationship between two graph entities."""

    source: str
    target: str
    relation: str
    evidence: str | None = None
    weight: float = 1.0
    metadata: dict[str, Any] = field(default_factory=dict)
