from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Any


class ExecutionStatus(StrEnum):
    """Represents the outcome of an experiment execution."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass(slots=True)
class ExperimentExecution:
    """
    Records one execution of an Emergence Lab experiment.

    This object stores operational facts about a run. It does not
    interpret scientific meaning or determine whether a hypothesis
    has been supported.
    """

    run_identifier: str
    experiment_identifier: str
    status: ExecutionStatus
    started_at: datetime
    completed_at: datetime | None = None
    output: Any = None
    error_message: str | None = None