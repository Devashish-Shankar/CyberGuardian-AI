"""
CyberGuardian AI

Attack Knowledge Database
"""

from pathlib import Path
import json


class AttackDatabase:

    def __init__(
        self,
        database_path: str = "data/knowledge/attacks.json"
    ):

        self.database_path = Path(database_path)

        self.database = self._load()

    def _load(self):

        if not self.database_path.exists():
            raise FileNotFoundError(
                f"Knowledge file not found:\n{self.database_path}"
            )

        with open(self.database_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get(self, attack_name: str):

        return self.database.get(attack_name)

    def exists(self, attack_name: str):

        return attack_name in self.database

    def all_attacks(self):

        return list(self.database.keys())

    def size(self):

        return len(self.database)