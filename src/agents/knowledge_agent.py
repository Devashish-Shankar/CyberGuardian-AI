"""
==========================================================
CyberGuardian AI

Knowledge Agent

Responsible for retrieving structured cyber threat
intelligence from the Knowledge Module.

Author: Devashish
==========================================================
"""

from __future__ import annotations

from src.agents.base_agent import BaseAgent

from src.knowledge.attack_mapper import AttackMapper
from src.knowledge.severity import SeverityEngine
from src.knowledge.mitigation import MitigationEngine
from src.knowledge.mitre_loader import MitreLoader


class KnowledgeAgent(BaseAgent):
    """
    Converts an attack prediction into structured
    cybersecurity knowledge.
    """

    def __init__(self) -> None:

        self.mapper = AttackMapper()

        self.severity_engine = SeverityEngine()

        self.mitigation_engine = MitigationEngine()

        self.mitre_loader = MitreLoader()

    # =====================================================
    # Public API
    # =====================================================

    def run(
        self,
        prediction: dict
    ) -> dict:

        if not isinstance(prediction, dict):

            raise TypeError(
                "Prediction must be a dictionary."
            )

        if not prediction.get("is_attack"):

            return {

                "attack_name": "Benign",

                "severity": "None",

                "description": "No malicious activity detected.",

                "confidence": prediction.get(
                    "confidence",
                    0
                ),

                "category": "Normal Traffic",

                "symptoms": [],

                "impact": "No security impact.",

                "mitigation": [],

                "mitre_attack": [],

                "ioc": [],

                "references": []

            }

        attack_name = prediction["attack_name"]

        attack = self.mapper.map(
            attack_name
        )

        severity = self.severity_engine.get(
            attack
        )

        mitigation = self.mitigation_engine.get(
            attack
        )

        mitre = self.mitre_loader.get(
            attack
        )

        return {

            "attack_name": attack_name,

            "confidence": prediction[
                "confidence"
            ],

            "category": attack.get(
                "category"
            ),

            "severity": severity,

            "description": attack.get(
                "description"
            ),

            "symptoms": attack.get(
                "symptoms"
            ),

            "impact": attack.get(
                "impact"
            ),

            "detection": attack.get(
                "detection"
            ),

            "mitigation": mitigation,

            "mitre_attack": mitre,

            "ports": attack.get(
                "ports"
            ),

            "protocols": attack.get(
                "protocols"
            ),

            "ioc": attack.get(
                "ioc"
            ),

            "references": attack.get(
                "references"
            ),

            "top_predictions": prediction.get(
                "top_predictions",
                []
            )

        }