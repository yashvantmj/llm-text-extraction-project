"""
Anthropic (Claude) provider implementation for text extraction.
"""

from typing import Optional
from anthropic import Anthropic


class AnthropicProvider:
    """Provider class for Anthropic Claude API integration."""

    def __init__(self, api_key: str, model: str = "claude-3-sonnet-20240229"):
        """
        Initialize Anthropic provider.

        Args:
            api_key: Anthropic API key
            model: Model to use (default: claude-3-sonnet-20240229)
        """
        if not api_key:
            raise ValueError("Anthropic API key is required")

        self.client = Anthropic(api_key=api_key)
        self.model = model

    def complete(
        self,
        prompt: str,
        temperature: float = 0.1,
        max_tokens: int = 2000,
        system_message: Optional[str] = None,
    ) -> str:
        """
        Generate completion using Anthropic API.

        Args:
            prompt: User prompt
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response
            system_message: Optional system message

        Returns:
            Completion text
        """
        try:
            kwargs = {
                "model": self.model,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "messages": [{"role": "user", "content": prompt}],
            }

            if system_message:
                kwargs["system"] = system_message

            response = self.client.messages.create(**kwargs)

            return response.content[0].text

        except Exception as e:
            raise Exception(f"Anthropic API error: {str(e)}")
