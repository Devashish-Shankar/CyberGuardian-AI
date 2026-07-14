"""
CyberGuardian AI

Groq LLM Provider

Implements BaseLLM
"""

from __future__ import annotations

from groq import Groq

from src.llm.base_llm import BaseLLM
from src.prompts.security_prompt import SYSTEM_PROMPT
from src.config.config import (
    GROQ_API_KEY,
    MODEL_NAME
)


class GroqLLM(BaseLLM):
    """
    Groq implementation of BaseLLM.
    """

    def __init__(self) -> None:

        if not GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY not found in environment."
            )

        self.client: Groq = Groq(
            api_key=GROQ_API_KEY
        )

        self.model: str = MODEL_NAME

    def generate(
        self,
        prompt: str
    ) -> str:
        """
        Generate response from Groq LLM.

        Parameters
        ----------
        prompt : str
            User prompt.

        Returns
        -------
        str
            Generated response.
        """

        if not isinstance(prompt, str):
            raise TypeError(
                "Prompt must be a string."
            )

        if not prompt.strip():
            raise ValueError(
                "Prompt cannot be empty."
            )

        try:

            response = self.client.chat.completions.create(

                model=self.model,

                messages=[
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

            return response.choices[0].message.content.strip()

        except Exception as e:

            raise RuntimeError(
                f"Groq generation failed: {str(e)}"
            ) from e