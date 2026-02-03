"""
Tests for text extraction functionality.
"""

import pytest
from unittest.mock import Mock, patch
from src.text_extractor import TextExtractor
from src.extractors.invoice_extractor import InvoiceExtractor
from src.extractors.resume_extractor import ResumeExtractor


class TestTextExtractor:
    """Test cases for TextExtractor class."""

    def test_initialization_with_openai(self):
        """Test initialization with OpenAI provider."""
        with patch.dict(
            "os.environ",
            {"OPENAI_API_KEY": "test-key", "DEFAULT_PROVIDER": "openai"},
        ):
            extractor = TextExtractor(provider="openai")
            assert extractor.provider_name == "openai"

    def test_initialization_with_anthropic(self):
        """Test initialization with Anthropic provider."""
        with patch.dict(
            "os.environ",
            {"ANTHROPIC_API_KEY": "test-key", "DEFAULT_PROVIDER": "anthropic"},
        ):
            extractor = TextExtractor(provider="anthropic")
            assert extractor.provider_name == "anthropic"

    def test_invalid_provider(self):
        """Test that invalid provider raises ValueError."""
        with pytest.raises(ValueError):
            TextExtractor(provider="invalid_provider")

    @patch("src.text_extractor.OpenAIProvider")
    def test_extract_entities(self, mock_provider):
        """Test entity extraction."""
        mock_instance = Mock()
        mock_instance.complete.return_value = (
            '{"people": ["John Doe"], "organizations": ["Acme Corp"]}'
        )
        mock_provider.return_value = mock_instance

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            extractor = TextExtractor(provider="openai")
            result = extractor.extract_entities("Test text")

            assert "people" in result
            assert "organizations" in result

    @patch("src.text_extractor.OpenAIProvider")
    def test_summarize(self, mock_provider):
        """Test text summarization."""
        mock_instance = Mock()
        mock_instance.complete.return_value = "This is a test summary."
        mock_provider.return_value = mock_instance

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            extractor = TextExtractor(provider="openai")
            result = extractor.summarize("Long text here", length="short")

            assert result == "This is a test summary."

    @patch("src.text_extractor.OpenAIProvider")
    def test_analyze_sentiment(self, mock_provider):
        """Test sentiment analysis."""
        mock_instance = Mock()
        mock_instance.complete.return_value = """
        {
            "overall_sentiment": "positive",
            "confidence": 0.9,
            "emotions": ["joy", "excitement"],
            "key_phrases": ["love this", "amazing"],
            "reasoning": "Very positive language used"
        }
        """
        mock_provider.return_value = mock_instance

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            extractor = TextExtractor(provider="openai")
            result = extractor.analyze_sentiment("I love this!")

            assert result["overall_sentiment"] == "positive"
            assert result["confidence"] == 0.9

    @patch("src.text_extractor.OpenAIProvider")
    def test_classify_text(self, mock_provider):
        """Test text classification."""
        mock_instance = Mock()
        mock_instance.complete.return_value = '{"category": "technology"}'
        mock_provider.return_value = mock_instance

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            extractor = TextExtractor(provider="openai")
            result = extractor.classify_text(
                "AI news", categories=["technology", "sports", "politics"]
            )

            assert result == "technology"


class TestInvoiceExtractor:
    """Test cases for InvoiceExtractor class."""

    @patch("src.extractors.invoice_extractor.TextExtractor")
    def test_extract_invoice(self, mock_extractor):
        """Test invoice data extraction."""
        mock_instance = Mock()
        mock_instance.extract_structured_data.return_value = {
            "invoice_number": "INV-001",
            "total": 1000.00,
        }
        mock_extractor.return_value = mock_instance

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            extractor = InvoiceExtractor()
            result = extractor.extract("Invoice text")

            assert result["invoice_number"] == "INV-001"
            assert result["total"] == 1000.00

    def test_validate_invoice_valid(self):
        """Test validation of valid invoice data."""
        extractor = InvoiceExtractor()
        invoice_data = {
            "invoice_number": "INV-001",
            "total": 1100.00,
            "subtotal": 1000.00,
            "tax": 100.00,
            "vendor": {"name": "Test Vendor"},
            "customer": {"name": "Test Customer"},
        }

        result = extractor.validate_invoice(invoice_data)
        assert result["valid"] == True
        assert len(result["errors"]) == 0

    def test_validate_invoice_missing_fields(self):
        """Test validation with missing required fields."""
        extractor = InvoiceExtractor()
        invoice_data = {"invoice_number": "INV-001"}

        result = extractor.validate_invoice(invoice_data)
        assert result["valid"] == False
        assert len(result["errors"]) > 0


class TestResumeExtractor:
    """Test cases for ResumeExtractor class."""

    @patch("src.extractors.resume_extractor.TextExtractor")
    def test_extract_resume(self, mock_extractor):
        """Test resume data extraction."""
        mock_instance = Mock()
        mock_instance.extract_structured_data.return_value = {
            "personal_info": {"name": "John Doe", "email": "john@example.com"}
        }
        mock_extractor.return_value = mock_instance

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            extractor = ResumeExtractor()
            result = extractor.extract("Resume text")

            assert "personal_info" in result
            assert result["personal_info"]["name"] == "John Doe"

    @patch("src.extractors.resume_extractor.TextExtractor")
    def test_extract_contact_info(self, mock_extractor):
        """Test contact information extraction."""
        mock_instance = Mock()
        mock_instance.provider.complete.return_value = """
        {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "+1-555-1234"
        }
        """
        mock_extractor.return_value = mock_instance

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            extractor = ResumeExtractor()
            result = extractor.extract_contact_info("Resume text")

            assert result["name"] == "John Doe"
            assert result["email"] == "john@example.com"

    @patch("src.extractors.resume_extractor.TextExtractor")
    def test_extract_skills(self, mock_extractor):
        """Test skills extraction."""
        mock_instance = Mock()
        mock_instance.provider.complete.return_value = """
        {
            "technical": ["Python", "JavaScript"],
            "languages": ["English", "Spanish"],
            "tools": ["Git", "Docker"],
            "soft_skills": ["Leadership", "Communication"]
        }
        """
        mock_extractor.return_value = mock_instance

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            extractor = ResumeExtractor()
            result = extractor.extract_skills("Resume text")

            assert "technical" in result
            assert "Python" in result["technical"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
