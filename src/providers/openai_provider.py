"""
OpenAI provider implementation for text extraction.
"""

from typing import Optional
from openai import OpenAI


class OpenAIProvider:
    """Provider class for OpenAI API integration."""

    def __init__(self, api_key: str, model: str = "gpt-4-turbo-preview"):
        """
        Initialize OpenAI provider.

        Args:
            api_key: OpenAI API key
            model: Model to use (default: gpt-4-turbo-preview)
        """
        if not api_key:
            raise ValueError("OpenAI API key is required")

        self.client = OpenAI(api_key=api_key)
        self.model = model

    def complete(
        self,
        prompt: str,
        temperature: float = 0.1,
        max_tokens: int = 2000,
        system_message: Optional[str] = None,
    ) -> str:
        """
        Generate completion using OpenAI API.

        Args:
            prompt: User prompt
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response
            system_message: Optional system message

        Returns:
            Completion text
        """
        messages = []

        if system_message:
            messages.append({"role": "system", "content": system_message})

        messages.append({"role": "user", "content": prompt})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )

            return response.choices[0].message.content

        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")

    def complete_with_json(
        self,
        prompt: str,
        temperature: float = 0.1,
        max_tokens: int = 2000,
    ) -> str:
        """
        Generate completion with JSON mode enabled.

        Args:
            prompt: User prompt
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response

        Returns:
            JSON response
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
                response_format={"type": "json_object"},
            )

            return response.choices[0].message.content

        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
