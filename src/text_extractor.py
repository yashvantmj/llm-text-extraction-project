"""
Main text extraction and understanding module.
Provides a unified interface for various text extraction tasks using LLMs.
"""

import os
from typing import Dict, List, Optional, Union, Any
from dotenv import load_dotenv
import json

from .providers.openai_provider import OpenAIProvider
from .providers.anthropic_provider import AnthropicProvider

# Load environment variables
load_dotenv()


class TextExtractor:
    """
    Main class for text extraction and understanding using LLMs.
    Supports multiple providers and various extraction tasks.
    """

    def __init__(
        self,
        provider: str = None,
        api_key: str = None,
        model: str = None,
        temperature: float = 0.1,
        max_tokens: int = 2000,
    ):
        """
        Initialize the TextExtractor.

        Args:
            provider: LLM provider ('openai' or 'anthropic')
            api_key: API key for the provider
            model: Model name to use
            temperature: Sampling temperature (0.0 to 1.0)
            max_tokens: Maximum tokens in response
        """
        self.provider_name = provider or os.getenv("DEFAULT_PROVIDER", "openai")
        self.temperature = temperature
        self.max_tokens = max_tokens

        # Initialize the appropriate provider
        if self.provider_name == "openai":
            self.provider = OpenAIProvider(
                api_key=api_key or os.getenv("OPENAI_API_KEY"),
                model=model or os.getenv("OPENAI_MODEL", "gpt-4-turbo-preview"),
            )
        elif self.provider_name == "anthropic":
            self.provider = AnthropicProvider(
                api_key=api_key or os.getenv("ANTHROPIC_API_KEY"),
                model=model
                or os.getenv("ANTHROPIC_MODEL", "claude-3-sonnet-20240229"),
            )
        else:
            raise ValueError(
                f"Unsupported provider: {self.provider_name}. "
                "Use 'openai' or 'anthropic'."
            )

    def extract_entities(
        self, text: str, entity_types: Optional[List[str]] = None
    ) -> Dict[str, List[str]]:
        """
        Extract named entities from text.

        Args:
            text: Input text to extract entities from
            entity_types: List of entity types to extract (optional)

        Returns:
            Dictionary mapping entity types to lists of entities
        """
        default_types = [
            "people",
            "organizations",
            "locations",
            "dates",
            "money",
            "products",
        ]
        types = entity_types or default_types

        prompt = f"""Extract named entities from the following text and return them as a JSON object.

Entity types to extract: {', '.join(types)}

Text: {text}

Return ONLY a valid JSON object with entity types as keys and arrays of entities as values. Example format:
{{
  "people": ["John Doe", "Jane Smith"],
  "organizations": ["Company A"],
  "locations": ["New York"],
  "dates": ["January 2024"],
  "money": ["$1,000"],
  "products": ["Product X"]
}}"""

        response = self.provider.complete(
            prompt, temperature=self.temperature, max_tokens=self.max_tokens
        )

        try:
            # Parse JSON from response
            entities = json.loads(response)
            return entities
        except json.JSONDecodeError:
            # If JSON parsing fails, try to extract JSON from markdown code blocks
            if "```json" in response:
                json_start = response.find("```json") + 7
                json_end = response.find("```", json_start)
                json_str = response[json_start:json_end].strip()
                return json.loads(json_str)
            elif "```" in response:
                json_start = response.find("```") + 3
                json_end = response.find("```", json_start)
                json_str = response[json_start:json_end].strip()
                return json.loads(json_str)
            else:
                return {"error": "Failed to parse entities", "raw_response": response}

    def summarize(
        self,
        text: str,
        length: str = "medium",
        style: str = "paragraph",
        focus: Optional[str] = None,
    ) -> str:
        """
        Summarize a document.

        Args:
            text: Text to summarize
            length: 'short', 'medium', or 'long'
            style: 'paragraph', 'bullets', or 'executive'
            focus: Optional focus area for the summary

        Returns:
            Summary text
        """
        length_guidelines = {
            "short": "2-3 sentences",
            "medium": "1 paragraph (4-6 sentences)",
            "long": "2-3 paragraphs",
        }

        style_instructions = {
            "paragraph": "Write in clear, concise paragraphs.",
            "bullets": "Use bullet points for key information.",
            "executive": "Write as an executive summary with key takeaways.",
        }

        focus_text = f"\nFocus particularly on: {focus}" if focus else ""

        prompt = f"""Summarize the following text.

Length: {length_guidelines.get(length, length_guidelines['medium'])}
Style: {style_instructions.get(style, style_instructions['paragraph'])}{focus_text}

Text to summarize:
{text}

Summary:"""

        return self.provider.complete(
            prompt, temperature=self.temperature, max_tokens=self.max_tokens
        )

    def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """
        Analyze sentiment and emotional tone of text.

        Args:
            text: Text to analyze

        Returns:
            Dictionary with sentiment analysis results
        """
        prompt = f"""Analyze the sentiment and emotional tone of the following text.

Text: {text}

Return a JSON object with:
- overall_sentiment: "positive", "negative", or "neutral"
- confidence: 0.0 to 1.0
- emotions: list of detected emotions
- key_phrases: list of phrases that influenced the sentiment
- reasoning: brief explanation

Return ONLY valid JSON:"""

        response = self.provider.complete(
            prompt, temperature=self.temperature, max_tokens=self.max_tokens
        )

        try:
            sentiment = json.loads(response)
            return sentiment
        except json.JSONDecodeError:
            if "```json" in response:
                json_start = response.find("```json") + 7
                json_end = response.find("```", json_start)
                json_str = response[json_start:json_end].strip()
                return json.loads(json_str)
            elif "```" in response:
                json_start = response.find("```") + 3
                json_end = response.find("```", json_start)
                json_str = response[json_start:json_end].strip()
                return json.loads(json_str)
            else:
                return {"error": "Failed to parse sentiment", "raw_response": response}

    def extract_structured_data(
        self, text: str, schema: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Extract structured data based on a provided schema.

        Args:
            text: Text to extract data from
            schema: JSON schema describing the desired output structure

        Returns:
            Extracted data matching the schema
        """
        prompt = f"""Extract structured data from the following text according to the provided schema.

Schema:
{json.dumps(schema, indent=2)}

Text:
{text}

Return ONLY valid JSON matching the schema:"""

        response = self.provider.complete(
            prompt, temperature=self.temperature, max_tokens=self.max_tokens
        )

        try:
            data = json.loads(response)
            return data
        except json.JSONDecodeError:
            if "```json" in response:
                json_start = response.find("```json") + 7
                json_end = response.find("```", json_start)
                json_str = response[json_start:json_end].strip()
                return json.loads(json_str)
            elif "```" in response:
                json_start = response.find("```") + 3
                json_end = response.find("```", json_start)
                json_str = response[json_start:json_end].strip()
                return json.loads(json_str)
            else:
                return {"error": "Failed to parse data", "raw_response": response}

    def classify_text(
        self, text: str, categories: List[str], multi_label: bool = False
    ) -> Union[str, List[str]]:
        """
        Classify text into predefined categories.

        Args:
            text: Text to classify
            categories: List of possible categories
            multi_label: Whether to allow multiple categories

        Returns:
            Single category or list of categories
        """
        multi_label_instruction = (
            "The text can belong to multiple categories."
            if multi_label
            else "Choose only ONE category that best fits."
        )

        prompt = f"""Classify the following text into one or more of these categories:
{', '.join(categories)}

{multi_label_instruction}

Text: {text}

Return your answer as a JSON object:
{{"categories": ["category1", "category2"]}} for multi-label
OR
{{"category": "category1"}} for single-label

Return ONLY valid JSON:"""

        response = self.provider.complete(
            prompt, temperature=self.temperature, max_tokens=500
        )

        try:
            result = json.loads(response)
            if multi_label:
                return result.get("categories", [])
            else:
                return result.get("category", "")
        except json.JSONDecodeError:
            if "```json" in response:
                json_start = response.find("```json") + 7
                json_end = response.find("```", json_start)
                json_str = response[json_start:json_end].strip()
                result = json.loads(json_str)
                if multi_label:
                    return result.get("categories", [])
                else:
                    return result.get("category", "")
            else:
                return [] if multi_label else ""

    def extract_key_information(
        self, text: str, information_types: List[str]
    ) -> Dict[str, Any]:
        """
        Extract specific types of information from text.

        Args:
            text: Text to extract from
            information_types: Types of information to extract

        Returns:
            Dictionary with extracted information
        """
        prompt = f"""Extract the following information from the text:
{', '.join(information_types)}

Text:
{text}

Return the extracted information as a JSON object with the information types as keys.
Return ONLY valid JSON:"""

        response = self.provider.complete(
            prompt, temperature=self.temperature, max_tokens=self.max_tokens
        )

        try:
            info = json.loads(response)
            return info
        except json.JSONDecodeError:
            if "```json" in response:
                json_start = response.find("```json") + 7
                json_end = response.find("```", json_start)
                json_str = response[json_start:json_end].strip()
                return json.loads(json_str)
            elif "```" in response:
                json_start = response.find("```") + 3
                json_end = response.find("```", json_start)
                json_str = response[json_start:json_end].strip()
                return json.loads(json_str)
            else:
                return {"error": "Failed to parse information", "raw_response": response}
