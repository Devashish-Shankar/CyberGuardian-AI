import json


class MitreKnowledgeBase:

    def __init__(self,
                 path="data/external/mitre_attack_mapping.json"):

        with open(path, "r", encoding="utf-8") as f:
            self.database = json.load(f)

    def get_attack_info(self, attack_name):

        return self.database.get(
            attack_name,
            {
                "mitre_id": "Unknown",
                "mitre_name": "Unknown",
                "severity": "Unknown",
                "description": "No information available.",
                "impact": [],
                "recommendations": []
            }
        )