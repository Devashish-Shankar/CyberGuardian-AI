"""
Groq LLM Provider

Implements BaseLLM
"""

from groq import Groq

from prompts.security_prompt import SYSTEM_PROMPT
from src.llm.base_llm import BaseLLM
from src.config.config import (
    GROQ_API_KEY,
    MODEL_NAME
)


class GroqLLM(BaseLLM):

    def __init__(self):

        self.client = Groq(
            api_key=GROQ_API_KEY
        )

        self.model = MODEL_NAME

    def generate(
        self,
        prompt: str
    ) -> str:

        response = self.client.chat.completions.create(

            model=self.model,

            messages = [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2,

            max_tokens=1200

        )

        return response.choices[0].message.content