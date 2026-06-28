"""
==========================================
CyberGuardian AI

Explanation Agent

Author : Devashish
==========================================
"""

from src.knowledge.mitre_loader import MitreKnowledgeBase


class ExplanationAgent:

    def __init__(self):

        self.kb = MitreKnowledgeBase()

    def calculate_risk_score(
        self,
        confidence,
        severity
    ):
        """
        Calculate risk score using
        confidence + severity.
        """

        severity_weight = {
            "Critical": 100,
            "High": 80,
            "Medium": 60,
            "Low": 40,
            "Unknown": 20
        }

        base = severity_weight.get(
            severity,
            20
        )

        risk = (
            base * confidence
        )

        return round(risk, 2)

    def explain(
        self,
        attack_name,
        confidence
    ):

        info = self.kb.get_attack_info(
            attack_name
        )

        risk = self.calculate_risk_score(
            confidence,
            info["severity"]
        )

        response = {

            "attack_name": attack_name,

            "confidence": round(
                confidence * 100,
                2
            ),

            "severity": info["severity"],

            "mitre_id": info["mitre_id"],

            "mitre_name": info["mitre_name"],

            "description": info["description"],

            "impact": info["impact"],

            "recommendations": info[
                "recommendations"
            ],

            "risk_score": risk

        }

        return response


if __name__ == "__main__":

    agent = ExplanationAgent()

    output = agent.explain(

        attack_name="DDoS",

        confidence=0.998

    )

    print("\n")

    for key, value in output.items():

        print(f"{key}: {value}")