"""
Base LLM Interface

Every provider must inherit this class.
"""

from abc import ABC, abstractmethod


class BaseLLM(ABC):

    @abstractmethod
    def generate(
        self,
        prompt: str
    ) -> str:
        """
        Generate response from LLM.
        """
        pass