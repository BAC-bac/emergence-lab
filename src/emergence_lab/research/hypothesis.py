from __future__ import annotations

from dataclasses import dataclass, field

from emergence_lab.research.lineage import ResearchLineage


@dataclass(slots=True)
class Hypothesis:
    """
    Represents a testable hypothesis.
    """

    identifier: str
    statement: str
    rationale: str
    falsification_criteria: str
    lineage: ResearchLineage = field(default_factory=ResearchLineage)