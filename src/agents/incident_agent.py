"""
==========================================================
CyberGuardian AI

Incident Agent

Responsible for generating a complete cybersecurity
incident report using the LLM.

Author: Devashish
==========================================================
"""

from __future__ import annotations

from src.agents.base_agent import BaseAgent

from src.llm.llm_factory import LLMFactory

from src.prompts.report_prompt import REPORT_PROMPT


class IncidentAgent(BaseAgent):
    """
    Generates a complete incident report.
    """

    def __init__(self) -> None:

        self.llm = LLMFactory.create()

    # =====================================================
    # Helpers
    # =====================================================

    @staticmethod
    def _to_markdown(data) -> str:
        """
        Convert list or value into markdown.
        """

        if isinstance(data, list):

            return "\n".join(
                f"- {item}" for item in data
            )

        return str(data)

    # =====================================================
    # Public API
    # =====================================================

    def run(
        self,
        knowledge: dict,
        explainability: dict
    ) -> str:

        if not isinstance(knowledge, dict):

            raise TypeError(
                "knowledge must be a dictionary."
            )

        if not isinstance(explainability, dict):

            raise TypeError(
                "explainability must be a dictionary."
            )

        prompt = REPORT_PROMPT.format(

            attack_name=knowledge["attack_name"],

            category=knowledge["category"],

            severity=knowledge["severity"],

            confidence=knowledge["confidence"],

            description=knowledge["description"],

            top_features=self._to_markdown(
                explainability["top_features"]
            ),

            shap_explanation=explainability[
                "narrative"
            ],

            symptoms=self._to_markdown(
                knowledge["symptoms"]
            ),

            ioc=self._to_markdown(
                knowledge["ioc"]
            ),

            mitre_attack=self._to_markdown(
                knowledge["mitre_attack"]
            ),

            impact=self._to_markdown(
                knowledge["impact"]
            ),

            mitigation=self._to_markdown(
                knowledge["mitigation"]
            )

        )

        return self.llm.generate(prompt)