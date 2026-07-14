"""
CyberGuardian AI

Base LLM Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Abstract interface for all LLM providers.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str
    ) -> str:
        """
        Generate a response from the LLM.
        """
        pass