from emergence_lab.research import (
    Conclusion,
    ConclusionConfidence,
    ResearchLineage,
)


def test_conclusion_preserves_supporting_evidence_and_uncertainty() -> None:
    conclusion = Conclusion(
        identifier="CON-0001",
        statement=(
            "The baseline agent's behaviour is consistent with random movement "
            "under the tested conditions."
        ),
        confidence=ConclusionConfidence.TENTATIVE,
        supporting_result_ids=["RES-0001"],
        alternative_explanations=[
            "The apparent randomness may depend on the selected random seed.",
            "The experiment may be too short to reveal longer-term structure.",
        ],
        limitations=[
            "Only one agent architecture was tested.",
            "No comparison against alternative stochastic processes was performed.",
        ],
        lineage=ResearchLineage(parent_ids=["RES-0001"]),
    )

    assert conclusion.identifier == "CON-0001"
    assert conclusion.confidence is ConclusionConfidence.TENTATIVE
    assert conclusion.supporting_result_ids == ["RES-0001"]
    assert len(conclusion.alternative_explanations) == 2
    assert conclusion.lineage.parent_ids == ["RES-0001"]