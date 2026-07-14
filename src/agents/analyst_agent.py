"""
==========================================================
CyberGuardian AI

Analyst Agent

Responsible for generating professional SOC analysis
using the LLM module.

Author: Devashish
==========================================================
"""

from __future__ import annotations

from src.agents.base_agent import BaseAgent

from src.llm.llm_factory import LLMFactory

from src.prompts.analyst_prompt import ANALYST_PROMPT


class AnalystAgent(BaseAgent):
    """
    Generates professional cybersecurity analysis
    using structured threat intelligence.
    """

    def __init__(self) -> None:

        self.llm = LLMFactory.create()

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

        prompt = ANALYST_PROMPT.format(

            attack_name=knowledge["attack_name"],

            severity=knowledge["severity"],

            confidence=knowledge["confidence"],

            description=knowledge["description"],

            top_features=explainability["top_features"],

            symptoms=knowledge["symptoms"],

            impact=knowledge["impact"],

            mitigation=knowledge["mitigation"]

        )

        response = self.llm.generate(
            prompt
        )

        return response