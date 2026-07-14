from __future__ import annotations

from emergence_lab.engine import ExecutionStatus, ExperimentEngine
from emergence_lab.research import Experiment, ResearchLineage


class SuccessfulExperiment(Experiment):
    """Small test experiment that completes successfully."""

    def execute(self) -> dict[str, int]:
        return {"observations": 10}


class FailingExperiment(Experiment):
    """Small test experiment that deliberately fails."""

    def execute(self) -> None:
        raise RuntimeError("Deliberate test failure.")


def build_experiment(
    experiment_type: type[Experiment],
    identifier: str,
) -> Experiment:
    return experiment_type(
        identifier=identifier,
        question_identifier="RQ-0001",
        hypothesis_identifier="H-0001",
        title="Test experiment",
        description="Used to validate the experiment engine.",
        lineage=ResearchLineage(
            parent_ids=["RQ-0001", "H-0001"],
        ),
    )


def test_engine_records_successful_execution() -> None:
    engine = ExperimentEngine()
    experiment = build_experiment(
        SuccessfulExperiment,
        identifier="EXP-0001",
    )

    execution = engine.execute(experiment)

    assert execution.status is ExecutionStatus.COMPLETED
    assert execution.experiment_identifier == "EXP-0001"
    assert execution.output == {"observations": 10}
    assert execution.error_message is None
    assert execution.completed_at is not None


def test_engine_preserves_failed_execution() -> None:
    engine = ExperimentEngine()
    experiment = build_experiment(
        FailingExperiment,
        identifier="EXP-0002",
    )

    execution = engine.execute(experiment)

    assert execution.status is ExecutionStatus.FAILED
    assert execution.output is None
    assert execution.error_message == (
        "RuntimeError: Deliberate test failure."
    )
    assert execution.completed_at is not None


def test_engine_creates_distinct_run_identifiers() -> None:
    engine = ExperimentEngine()
    experiment = build_experiment(
        SuccessfulExperiment,
        identifier="EXP-0001",
    )

    first_execution = engine.execute(experiment)
    second_execution = engine.execute(experiment)

    assert first_execution.run_identifier != second_execution.run_identifier