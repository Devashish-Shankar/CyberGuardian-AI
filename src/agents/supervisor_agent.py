"""
==========================================================
CyberGuardian AI

Supervisor Agent

Responsible for orchestrating the complete AI pipeline.

Author: Devashish
==========================================================
"""

from __future__ import annotations

import pandas as pd

from src.agents.base_agent import BaseAgent
from src.agents.prediction_agent import PredictionAgent
from src.agents.knowledge_agent import KnowledgeAgent
from src.agents.explainability_agent import ExplainabilityAgent
from src.agents.analyst_agent import AnalystAgent
from src.agents.incident_agent import IncidentAgent


class SupervisorAgent(BaseAgent):
    """
    Orchestrates the complete CyberGuardian AI pipeline.
    """

    def __init__(self) -> None:

        self.prediction_agent = PredictionAgent()

        self.knowledge_agent = KnowledgeAgent()

        self.explainability_agent = ExplainabilityAgent()

        self.analyst_agent = AnalystAgent()

        self.incident_agent = IncidentAgent()

    # =====================================================
    # Public API
    # =====================================================

    def run(
        self,
        sample: pd.DataFrame
    ) -> dict:
        """
        Execute the complete CyberGuardian AI pipeline.
        """

        # -------------------------------------------------
        # Step 1 : Prediction
        # -------------------------------------------------

        prediction = self.prediction_agent.run(
            sample
        )

        # -------------------------------------------------
        # Benign Traffic
        # -------------------------------------------------

        if not prediction["is_attack"]:

            return {

                "status": "safe",

                "prediction": prediction,

                "knowledge": None,

                "explainability": None,

                "analysis": None,

                "incident_report": None

            }

        # -------------------------------------------------
        # Step 2 : Knowledge
        # -------------------------------------------------

        knowledge = self.knowledge_agent.run(
            prediction
        )

        # -------------------------------------------------
        # Step 3 : Explainability
        # -------------------------------------------------

        explainability = self.explainability_agent.run(
            sample
        )

        # -------------------------------------------------
        # Step 4 : AI Analysis
        # -------------------------------------------------

        analysis = self.analyst_agent.run(

            knowledge,

            explainability

        )

        # -------------------------------------------------
        # Step 5 : Incident Report
        # -------------------------------------------------

        incident_report = self.incident_agent.run(

            knowledge,

            explainability

        )

        # -------------------------------------------------
        # Final Response
        # -------------------------------------------------

        return {

            "status": "attack_detected",

            "prediction": prediction,

            "knowledge": knowledge,

            "explainability": explainability,

            "analysis": analysis,

            "incident_report": incident_report

        }