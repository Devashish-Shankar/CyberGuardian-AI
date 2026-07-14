"""
==========================================================
CyberGuardian AI

Agents Module Test

Tests

1. Base Agent
2. Prediction Agent
3. Knowledge Agent
4. Explainability Agent
5. Analyst Agent
6. Incident Agent
7. Supervisor Agent
8. End-to-End Pipeline

Author : Devashish
==========================================================
"""

from pathlib import Path

import pandas as pd

from src.agents.base_agent import BaseAgent
from src.agents.prediction_agent import PredictionAgent
from src.agents.knowledge_agent import KnowledgeAgent
from src.agents.explainability_agent import ExplainabilityAgent
from src.agents.analyst_agent import AnalystAgent
from src.agents.incident_agent import IncidentAgent
from src.agents.supervisor_agent import SupervisorAgent


# ==========================================================
# Test Data
# ==========================================================

DATASET_PATH = Path(
    "data/processed/clean_cicids.parquet"
)


def load_sample():

    df = pd.read_parquet(
        DATASET_PATH
    )

    sample = df.drop(

        columns=[

            "Label",

            "attack_category",

            "target"

        ]

    ).iloc[[36666]]

    return sample


# ==========================================================
# Base Agent
# ==========================================================

def test_base_agent():

    print("=" * 70)
    print("Testing Base Agent")
    print("=" * 70)

    assert issubclass(
        PredictionAgent,
        BaseAgent
    )

    assert issubclass(
        KnowledgeAgent,
        BaseAgent
    )

    assert issubclass(
        ExplainabilityAgent,
        BaseAgent
    )

    assert issubclass(
        AnalystAgent,
        BaseAgent
    )

    assert issubclass(
        IncidentAgent,
        BaseAgent
    )

    assert issubclass(
        SupervisorAgent,
        BaseAgent
    )

    print("✓ Base Agent Passed\n")


# ==========================================================
# Prediction Agent
# ==========================================================

def test_prediction_agent():

    print("=" * 70)
    print("Testing Prediction Agent")
    print("=" * 70)

    sample = load_sample()

    agent = PredictionAgent()

    result = agent.run(
        sample
    )

    assert isinstance(
        result,
        dict
    )

    assert "is_attack" in result

    assert "confidence" in result

    assert "attack_name" in result

    print(result)

    print()

    print("✓ Prediction Agent Passed\n")

    return result, sample


# ==========================================================
# Knowledge Agent
# ==========================================================

def test_knowledge_agent(
    prediction_result
):

    print("=" * 70)
    print("Testing Knowledge Agent")
    print("=" * 70)

    agent = KnowledgeAgent()

    result = agent.run(
        prediction_result
    )

    assert isinstance(
        result,
        dict
    )

    assert "severity" in result

    assert "description" in result

    assert "mitigation" in result

    assert "mitre_attack" in result

    print()

    print(

        f"Attack : {result['attack_name']}"

    )

    print(

        f"Severity : {result['severity']}"

    )

    print()

    print("✓ Knowledge Agent Passed\n")

    return result


# ==========================================================
# Explainability Agent
# ==========================================================

def test_explainability_agent(
    sample
):

    print("=" * 70)
    print("Testing Explainability Agent")
    print("=" * 70)

    agent = ExplainabilityAgent()

    result = agent.run(
        sample
    )

    assert isinstance(
        result,
        dict
    )

    assert "top_features" in result

    assert "narrative" in result

    print()

    print(

        "Top Features :"

    )

    print(

        result["top_features"]

    )

    print()

    print("✓ Explainability Agent Passed\n")

    return result

# ==========================================================
# Analyst Agent
# ==========================================================

def test_analyst_agent(
    knowledge,
    explainability
):

    print("=" * 70)
    print("Testing Analyst Agent")
    print("=" * 70)

    agent = AnalystAgent()

    report = agent.run(

        knowledge,

        explainability

    )

    assert isinstance(
        report,
        str
    )

    assert len(report) > 100

    print()

    print(report[:600])

    print()

    print("✓ Analyst Agent Passed\n")

    return report


# ==========================================================
# Incident Agent
# ==========================================================

def test_incident_agent(
    knowledge,
    explainability
):

    print("=" * 70)
    print("Testing Incident Agent")
    print("=" * 70)

    agent = IncidentAgent()

    report = agent.run(

        knowledge,

        explainability

    )

    assert isinstance(
        report,
        str
    )

    assert len(report) > 100

    print()

    print(report[:600])

    print()

    print("✓ Incident Agent Passed\n")

    return report


# ==========================================================
# Supervisor Agent
# ==========================================================

def test_supervisor_agent(
    sample
):

    print("=" * 70)
    print("Testing Supervisor Agent")
    print("=" * 70)

    agent = SupervisorAgent()

    result = agent.run(
        sample
    )

    assert isinstance(
        result,
        dict
    )

    assert "status" in result

    print()

    print("Pipeline Status :")

    print(result["status"])

    print()

    print("✓ Supervisor Agent Passed\n")

    return result


# ==========================================================
# End-to-End Pipeline
# ==========================================================

def test_end_to_end():

    print("=" * 70)
    print("Testing Complete AI Pipeline")
    print("=" * 70)

    prediction, sample = test_prediction_agent()

    knowledge = test_knowledge_agent(
        prediction
    )

    if prediction["is_attack"]:

        explainability = test_explainability_agent(
            sample
        )

        test_analyst_agent(

            knowledge,

            explainability

        )

        test_incident_agent(

            knowledge,

            explainability

        )

    test_supervisor_agent(
        sample
    )

    print()

    print("✓ End-to-End Pipeline Passed\n")


# ==========================================================
# Main
# ==========================================================

def main():

    print("\n")

    print("=" * 70)
    print("CyberGuardian AI")
    print("Agents Module Test")
    print("=" * 70)

    test_base_agent()

    test_end_to_end()

    print("=" * 70)
    print("ALL AGENT TESTS PASSED")
    print("=" * 70)


if __name__ == "__main__":

    main()