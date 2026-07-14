from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from emergence_lab.research.lineage import ResearchLineage


@dataclass(slots=True)
class Experiment(ABC):
    """
    Base class for an Emergence Lab scientific experiment.

    An experiment defines what will be executed. Operational execution
    details are handled separately by ExperimentEngine.
    """

    identifier: str
    question_identifier: str
    hypothesis_identifier: str
    title: str
    description: str
    lineage: ResearchLineage = field(default_factory=ResearchLineage)

    @abstractmethod
    def execute(self) -> Any:
        """Execute the experiment and return its raw output."""