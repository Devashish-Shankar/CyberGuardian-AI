from src.config.config import LLM_PROVIDER

from src.llm.groq_llm import GroqLLM


class LLMFactory:

    @staticmethod
    def get_llm():

        if LLM_PROVIDER.lower() == "groq":
            return GroqLLM()

        raise ValueError(
            f"Unsupported LLM Provider: {LLM_PROVIDER}"
        )