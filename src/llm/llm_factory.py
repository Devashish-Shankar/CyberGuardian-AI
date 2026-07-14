"""
CyberGuardian AI

LLM Factory
"""

from src.config.config import LLM_PROVIDER

from src.llm.groq_llm import GroqLLM


class LLMFactory:

    @staticmethod
    def create():

        if not LLM_PROVIDER:

            raise ValueError(
                "LLM_PROVIDER is not configured."
            )

        provider = LLM_PROVIDER.lower().strip()

        if provider == "groq":

            return GroqLLM()

        raise ValueError(
            f"Unsupported LLM Provider: {LLM_PROVIDER}"
        )