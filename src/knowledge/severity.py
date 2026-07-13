"""
CyberGuardian AI

Severity Engine

Responsibility
--------------
Extract severity information from an attack object.
"""

from __future__ import annotations


class SeverityEngine:

    """
    Returns severity level for an attack.
    """

    def get(
        self,
        attack: dict
    ) -> str:

        if attack is None:

            raise ValueError(
                "Attack object cannot be None."
            )

        if not isinstance(attack, dict):

            raise TypeError(
                "Attack must be a dictionary."
            )

        severity = attack.get("severity")

        if severity is None:

            raise ValueError(
                "Severity not found."
            )

        return severity