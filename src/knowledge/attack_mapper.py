"""
CyberGuardian AI

Attack Mapper

Responsibility
--------------
Maps an attack name to its corresponding
knowledge base entry.
"""

from __future__ import annotations

from src.knowledge.attack_database import AttackDatabase


class AttackMapper:

    """
    Maps attack names to attack knowledge.
    """

    def __init__(self):

        self.database = AttackDatabase()

    def map(
        self,
        attack_name: str
    ) -> dict:

        if not isinstance(attack_name, str):

            raise TypeError(
                "attack_name must be a string."
            )

        attack = self.database.get(
            attack_name
        )

        if attack is None:

            raise ValueError(

                f"Unknown attack: {attack_name}"

            )

        return attack