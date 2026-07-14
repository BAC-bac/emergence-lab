from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum

from emergence_lab.research.lineage import ResearchLineage


class ConclusionConfidence(StrEnum):
    """
    Describes the strength of confidence attached to a conclusion.

    These labels represent cautious scientific judgement rather than
    formal statistical confidence levels.
    """

    SPECULATIVE = "speculative"
    TENTATIVE = "tentative"
    SUPPORTED = "supported"
    STRONGLY_SUPPORTED = "strongly_supported"


@dataclass(slots=True)
class Conclusion:
    """
    Represents a cautious scientific interpretation of one or more results.

    A conclusion is distinct from an observation or result:

    - An observation records what occurred.
    - A result summarises or measures what occurred.
    - A conclusion interprets what the result may mean.

    Conclusions must remain proportional to the available evidence.
    """

    identifier: str
    statement: str
    confidence: ConclusionConfidence
    supporting_result_ids: list[str] = field(default_factory=list)
    alternative_explanations: list[str] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)
    lineage: ResearchLineage = field(default_factory=ResearchLineage)