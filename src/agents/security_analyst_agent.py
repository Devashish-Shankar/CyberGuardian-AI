"""
CyberGuardian AI

Security Analyst Agent

This agent converts structured threat intelligence
into a professional SOC analyst report using an LLM.
"""

from src.llm.llm_factory import LLMFactory


class SecurityAnalystAgent:

    def __init__(self):

        self.llm = LLMFactory.get_llm()

    def analyze(
        self,
        threat_data: dict
    ) -> str:

        prompt = f"""

You are a Senior SOC Analyst.

Analyze the following cyber threat.

Attack Name:
{threat_data['attack_name']}

Confidence:
{threat_data['confidence']} %

Severity:
{threat_data['severity']}

MITRE Technique:
{threat_data['mitre_id']}

MITRE Name:
{threat_data['mitre_name']}

Description:
{threat_data['description']}

Impact:
{', '.join(threat_data['impact'])}

Recommendations:
{', '.join(threat_data['recommendations'])}

Generate a professional report.

Use the following headings.

# Executive Summary

# Technical Analysis

# MITRE ATT&CK

# Business Impact

# Recommendations

Use Markdown.
"""

        return self.llm.generate(prompt)


if __name__ == "__main__":

    sample = {

        "attack_name": "DDoS",

        "confidence": 99.8,

        "severity": "Critical",

        "mitre_id": "T1498",

        "mitre_name": "Network Denial of Service",

        "description":
        "Floods a target server with excessive traffic.",

        "impact": [

            "Service disruption",

            "Bandwidth exhaustion",

            "Business downtime"

        ],

        "recommendations": [

            "Enable WAF",

            "Block malicious IPs",

            "Rate limiting"

        ]

    }

    agent = SecurityAnalystAgent()

    report = agent.analyze(sample)

    print(report)