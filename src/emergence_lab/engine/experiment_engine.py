from __future__ import annotations

from datetime import UTC, datetime
from itertools import count
from typing import Any

from emergence_lab.engine.execution import (
    ExecutionStatus,
    ExperimentExecution,
)
from emergence_lab.research.experiment import Experiment


class ExperimentEngine:
    """
    Executes Emergence Lab experiments and records their operational outcome.

    The engine coordinates execution only. It does not interpret results,
    assess hypotheses, or produce scientific conclusions.
    """

    def __init__(self) -> None:
        self._run_counter = count(start=1)

    def execute(self, experiment: Experiment) -> ExperimentExecution:
        """
        Execute an experiment and return a traceable execution record.

        Exceptions are captured inside the execution record so failed runs
        remain part of the research history rather than disappearing.
        """

        self._validate_experiment(experiment)

        started_at = datetime.now(UTC)
        run_identifier = self._create_run_identifier(
            experiment_identifier=experiment.identifier,
            started_at=started_at,
        )

        execution = ExperimentExecution(
            run_identifier=run_identifier,
            experiment_identifier=experiment.identifier,
            status=ExecutionStatus.RUNNING,
            started_at=started_at,
        )

        try:
            execution.output = experiment.execute()
            execution.status = ExecutionStatus.COMPLETED
        except Exception as exc:
            execution.status = ExecutionStatus.FAILED
            execution.error_message = f"{type(exc).__name__}: {exc}"
        finally:
            execution.completed_at = datetime.now(UTC)

        return execution

    @staticmethod
    def _validate_experiment(experiment: Experiment) -> None:
        """Validate the minimum properties required for execution."""

        if not experiment.identifier.strip():
            raise ValueError("Experiment identifier cannot be empty.")

        if not experiment.question_identifier.strip():
            raise ValueError("Experiment question identifier cannot be empty.")

        if not experiment.hypothesis_identifier.strip():
            raise ValueError("Experiment hypothesis identifier cannot be empty.")

    def _create_run_identifier(
        self,
        experiment_identifier: str,
        started_at: datetime,
    ) -> str:
        """Create a unique, readable identifier for one execution."""

        sequence = next(self._run_counter)
        timestamp = started_at.strftime("%Y%m%dT%H%M%S%fZ")

        return f"{experiment_identifier}-{timestamp}-{sequence:04d}"