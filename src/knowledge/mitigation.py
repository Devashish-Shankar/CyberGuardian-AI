"""
CyberGuardian AI

Mitigation Engine

Responsibility
--------------
Extract mitigation recommendations
from an attack object.
"""

from __future__ import annotations


class MitigationEngine:
    """
    Returns mitigation steps for an attack.
    """

    def get(
        self,
        attack: dict
    ) -> list[str]:

        if attack is None:
            raise ValueError(
                "Attack object cannot be None."
            )

        if not isinstance(attack, dict):
            raise TypeError(
                "Attack must be a dictionary."
            )

        mitigation = attack.get("mitigation")

        if mitigation is None:
            raise ValueError(
                "Mitigation not found."
            )

        if not isinstance(mitigation, list):
            raise TypeError(
                "Mitigation must be a list."
            )

        return mitigation