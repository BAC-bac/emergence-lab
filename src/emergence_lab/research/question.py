from __future__ import annotations

from dataclasses import dataclass, field

from emergence_lab.research.lineage import ResearchLineage


@dataclass(slots=True)
class ResearchQuestion:
    """
    Represents a scientific question investigated by Emergence Lab.
    """

    identifier: str
    title: str
    description: str
    lineage: ResearchLineage = field(default_factory=ResearchLineage)