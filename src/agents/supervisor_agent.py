"""
CyberGuardian AI

Supervisor Agent

This is the orchestrator of the complete AI pipeline.
"""

from src.agents.binary_agent import BinaryDetectionAgent
from src.agents.multiclass_agent import MultiClassDetectionAgent
from src.agents.explanation_agent import ExplanationAgent
from src.agents.security_analyst_agent import SecurityAnalystAgent


class SupervisorAgent:

    def __init__(self):

        self.binary_agent = BinaryDetectionAgent()

        self.multiclass_agent = MultiClassDetectionAgent()

        self.explanation_agent = ExplanationAgent()

        self.security_agent = SecurityAnalystAgent()

    def analyze(self, sample):

        print("Running Binary Detection...")

        binary_result = self.binary_agent.detect(sample)

        if binary_result["prediction"] == 0:

            return {

                "status": "Safe",

                "message": "No cyber attack detected.",

                "confidence": round(
                    binary_result["confidence"] * 100,
                    2
                )

            }

        print("Attack Detected")

        print("Running Multi-Class Detection...")

        attack_result = self.multiclass_agent.detect(sample)

        print("Generating Threat Intelligence...")

        explanation = self.explanation_agent.explain(

            attack_name=attack_result["attack_name"],

            confidence=attack_result["confidence"] / 100

        )

        print("Generating AI Security Report...")

        analyst_report = self.security_agent.analyze(
            explanation
        )

        return {

            "binary_detection": binary_result,

            "attack_prediction": attack_result,

            "threat_intelligence": explanation,

            "security_report": analyst_report

        }