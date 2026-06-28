from src.llm.llm_factory import LLMFactory

llm = LLMFactory.get_llm()

response = llm.generate(

"""
Explain what is a DDoS attack
in less than 100 words.
"""

)

print(response)