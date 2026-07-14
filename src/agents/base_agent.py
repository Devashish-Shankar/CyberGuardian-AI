"""
CyberGuardian AI

Base Agent
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Base class for every AI agent.
    """

    @abstractmethod
    def run(self, *args, **kwargs):
        """
        Execute the agent.
        """
        pass