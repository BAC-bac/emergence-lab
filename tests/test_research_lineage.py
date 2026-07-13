from emergence_lab.research import Hypothesis, ResearchLineage, ResearchQuestion


def test_question_can_generate_hypothesis_lineage() -> None:
    question = ResearchQuestion(
        identifier="RQ-0001",
        title="Baseline behaviour",
        description="What behaviour exists before perception or memory?",
    )

    hypothesis = Hypothesis(
        identifier="H-0001",
        statement="An agent without perception or memory will behave randomly.",
        rationale="The agent has no information with which to favour one action.",
        falsification_criteria=(
            "The hypothesis is weakened if repeatable non-random structure appears "
            "without environmental information or internal state."
        ),
        lineage=ResearchLineage(parent_ids=[question.identifier]),
    )

    assert hypothesis.lineage.parent_ids == ["RQ-0001"]