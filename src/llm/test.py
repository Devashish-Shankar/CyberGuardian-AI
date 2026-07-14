"""
CyberGuardian AI

LLM Module Test

Tests:
1. Base LLM
2. Groq Provider
3. LLM Factory
4. End-to-End Generation
"""

from src.llm.base_llm import BaseLLM
from src.llm.groq_llm import GroqLLM
from src.llm.llm_factory import LLMFactory


TEST_PROMPT = """
Explain a Distributed Denial of Service (DDoS) attack.

Include:

- Definition
- Business Impact
- MITRE ATT&CK relevance
- Recommended Mitigation

Respond professionally.
"""


# ==========================================================
# Base LLM
# ==========================================================

def test_base():

    print("=" * 70)
    print("Testing Base LLM")
    print("=" * 70)
    print()

    assert issubclass(GroqLLM, BaseLLM)

    print("✓ GroqLLM inherits BaseLLM")
    print("✓ Base LLM Passed")
    print()


# ==========================================================
# Groq Provider
# ==========================================================

def test_groq():

    print("=" * 70)
    print("Testing Groq Provider")
    print("=" * 70)
    print()

    llm = GroqLLM()

    response = llm.generate(TEST_PROMPT)

    assert isinstance(response, str)
    assert len(response) > 50

    print(response[:500])
    print()

    print("✓ Response Generated")
    print("✓ Groq Provider Passed")
    print()


# ==========================================================
# Factory
# ==========================================================

def test_factory():

    print("=" * 70)
    print("Testing LLM Factory")
    print("=" * 70)
    print()

    llm = LLMFactory.create()

    print("Returned Object :", type(llm).__name__)

    assert isinstance(llm, BaseLLM)

    print()

    print("✓ Factory Returned Correct Provider")
    print("✓ Factory Passed")
    print()


# ==========================================================
# End-to-End
# ==========================================================

def test_end_to_end():

    print("=" * 70)
    print("Testing End-to-End Pipeline")
    print("=" * 70)
    print()

    llm = LLMFactory.create()

    response = llm.generate(TEST_PROMPT)

    print(response[:700])

    assert len(response) > 100

    print()

    print("✓ End-to-End Pipeline Passed")
    print()


# ==========================================================
# Main
# ==========================================================

def main():

    print("\n")
    print("=" * 70)
    print("CyberGuardian AI")
    print("LLM Module Test")
    print("=" * 70)
    print()

    test_base()

    test_groq()

    test_factory()

    test_end_to_end()

    print("=" * 70)
    print("ALL LLM TESTS PASSED")
    print("=" * 70)


if __name__ == "__main__":

    main()