"""
CyberGuardian AI

Prompts Module Test
"""

from src.prompts.security_prompt import SYSTEM_PROMPT
from src.prompts.analyst_prompt import ANALYST_PROMPT
from src.prompts.incident_prompt import INCIDENT_PROMPT
from src.prompts.executive_prompt import EXECUTIVE_PROMPT
from src.prompts.report_prompt import REPORT_PROMPT
from src.prompts.summary_prompt import SUMMARY_PROMPT


SAMPLE_DATA = {

    "attack_name": "DDoS",

    "category": "Distributed Denial of Service",

    "severity": "Critical",

    "confidence": "99.72%",

    "description": (
        "The target server is overwhelmed with a high volume "
        "of malicious network traffic."
    ),

    "top_features": (
        "Flow Duration, Packet Length Mean, "
        "Flow Bytes/s"
    ),

    "shap_explanation": (
        "Flow Duration and Flow Bytes/s contributed "
        "most strongly to the prediction."
    ),

    "symptoms": (
        "High traffic volume, packet flood, "
        "service degradation."
    ),

    "impact": (
        "Service disruption and reduced availability "
        "for legitimate users."
    ),

    "mitigation": (
        "- Enable rate limiting\n"
        "- Deploy WAF\n"
        "- Block malicious IP addresses"
    ),

    "mitre_attack": "T1498",

    "ioc": (
        "- Large number of SYN packets\n"
        "- Abnormal traffic spike\n"
        "- Multiple source IP addresses"
    )
}


# =====================================================
# Helper
# =====================================================

def validate_prompt(name: str, prompt: str):

    print("=" * 70)
    print(f"Testing {name}")
    print("=" * 70)

    formatted = prompt.format(**SAMPLE_DATA)

    assert isinstance(formatted, str)
    assert len(formatted) > 100

    print("Characters :", len(formatted))
    print("Status      : PASSED\n")


# =====================================================
# Individual Tests
# =====================================================

def test_security_prompt():

    print("=" * 70)
    print("Testing Security Prompt")
    print("=" * 70)

    assert isinstance(SYSTEM_PROMPT, str)
    assert len(SYSTEM_PROMPT) > 50

    print("Characters :", len(SYSTEM_PROMPT))
    print("Status      : PASSED\n")


def test_analyst_prompt():
    validate_prompt(
        "Analyst Prompt",
        ANALYST_PROMPT
    )


def test_incident_prompt():
    validate_prompt(
        "Incident Prompt",
        INCIDENT_PROMPT
    )


def test_executive_prompt():
    validate_prompt(
        "Executive Prompt",
        EXECUTIVE_PROMPT
    )


def test_report_prompt():
    validate_prompt(
        "Report Prompt",
        REPORT_PROMPT
    )


def test_summary_prompt():
    validate_prompt(
        "Summary Prompt",
        SUMMARY_PROMPT
    )


# =====================================================
# Main
# =====================================================

def main():

    print("\n")
    print("=" * 70)
    print("CyberGuardian AI")
    print("Prompts Module Test")
    print("=" * 70)
    print()

    test_security_prompt()

    test_analyst_prompt()

    test_incident_prompt()

    test_executive_prompt()

    test_report_prompt()

    test_summary_prompt()

    print("=" * 70)
    print("ALL PROMPT TESTS PASSED")
    print("=" * 70)


if __name__ == "__main__":

    main()