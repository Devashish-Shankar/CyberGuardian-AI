"""
CyberGuardian AI

Knowledge Loader

Responsibility
--------------
Load cyber attack knowledge from JSON.
"""

from __future__ import annotations

import json
from pathlib import Path


class KnowledgeLoader:

    """
    Loads the complete cyber attack
    knowledge base.
    """

    def __init__(
        self,
        knowledge_path: str = "data/knowledge/attacks.json"
    ):

        self.knowledge_path = Path(knowledge_path)

    def load(self) -> dict:

        if not self.knowledge_path.exists():

            raise FileNotFoundError(

                f"Knowledge base not found:\n"

                f"{self.knowledge_path}"

            )

        with open(

            self.knowledge_path,

            "r",

            encoding="utf-8"

        ) as file:

            knowledge = json.load(file)

        return knowledge