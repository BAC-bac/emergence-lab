from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ResearchLineage:
    """
    Records the intellectual lineage of a research object.

    Lineage allows Emergence Lab to trace how questions, hypotheses,
    experiments, observations, and results relate to one another.
    """

    parent_ids: list[str] = field(default_factory=list)
    related_ids: list[str] = field(default_factory=list)
    generated_ids: list[str] = field(default_factory=list)