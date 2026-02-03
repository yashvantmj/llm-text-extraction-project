# LLM Text Extraction & Understanding

A comprehensive Python project demonstrating text extraction and understanding using Large Language Models (LLMs). This project showcases practical applications of LLMs for various text processing tasks including entity extraction, document summarization, sentiment analysis, and structured data extraction.

## 🌟 Features

- **Entity Extraction**: Extract named entities (people, organizations, locations, dates, etc.)
- **Document Summarization**: Generate concise summaries of long documents
- **Sentiment Analysis**: Analyze sentiment and emotional tone
- **Structured Data Extraction**: Convert unstructured text to structured JSON
- **Invoice/Receipt Processing**: Extract key information from financial documents
- **Resume Parsing**: Extract structured information from resumes
- **Contract Analysis**: Identify key clauses and obligations
- **Multi-Provider Support**: Works with OpenAI, Anthropic (Claude), and local models

## 📋 Prerequisites

- Python 3.8+
- API keys for LLM providers (OpenAI or Anthropic)
- pip or poetry for dependency management

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/llm-text-extraction-project.git
cd llm-text-extraction-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```env
# Choose your LLM provider
OPENAI_API_KEY=your_openai_api_key_here
# OR
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Default provider (openai or anthropic)
DEFAULT_PROVIDER=openai
DEFAULT_MODEL=gpt-4-turbo-preview
```

### Basic Usage

```python
from src.text_extractor import TextExtractor

# Initialize the extractor
extractor = TextExtractor(provider="openai")

# Extract entities
text = "Apple Inc. announced a new product launch in Cupertino on March 15, 2024."
entities = extractor.extract_entities(text)
print(entities)

# Summarize document
long_text = "Your long document here..."
summary = extractor.summarize(long_text)
print(summary)
```

## 📁 Project Structure

```
llm-text-extraction-project/
├── src/
│   ├── __init__.py
│   ├── text_extractor.py      # Main extraction class
│   ├── providers/              # LLM provider integrations
│   │   ├── __init__.py
│   │   ├── openai_provider.py
│   │   └── anthropic_provider.py
│   ├── extractors/             # Specialized extractors
│   │   ├── __init__.py
│   │   ├── entity_extractor.py
│   │   ├── invoice_extractor.py
│   │   └── resume_extractor.py
│   └── utils/
│       ├── __init__.py
│       └── text_utils.py
├── examples/
│   ├── entity_extraction.py
│   ├── document_summarization.py
│   ├── invoice_processing.py
│   └── resume_parsing.py
├── data/
│   └── sample_documents/
├── tests/
│   ├── test_extractors.py
│   └── test_providers.py
├── docs/
│   └── API.md
├── requirements.txt
├── .env.example
└── README.md
```

## 🔧 Available Extractors

### 1. Entity Extraction
Extract named entities with categories and confidence scores:
- People, Organizations, Locations
- Dates, Times, Monetary Values
- Products, Events, Custom Entities

### 2. Document Summarization
Generate summaries with configurable:
- Length (short, medium, long)
- Style (bullet points, paragraph, executive summary)
- Focus areas

### 3. Sentiment Analysis
Analyze text for:
- Overall sentiment (positive/negative/neutral)
- Emotional tone
- Key themes and topics

### 4. Invoice/Receipt Processing
Extract structured data:
- Vendor information
- Line items with prices
- Totals, taxes, dates
- Payment terms

### 5. Resume Parsing
Extract candidate information:
- Contact details
- Work experience
- Education
- Skills and certifications

### 6. Contract Analysis
Identify:
- Parties involved
- Key terms and conditions
- Obligations and deadlines
- Risk factors

## 💡 Examples

### Entity Extraction

```python
from src.text_extractor import TextExtractor

extractor = TextExtractor()
text = """
Microsoft CEO Satya Nadella announced a $10 billion partnership 
with OpenAI in January 2023 at the company's Redmond headquarters.
"""

entities = extractor.extract_entities(text)
# Returns: {
#   "people": ["Satya Nadella"],
#   "organizations": ["Microsoft", "OpenAI"],
#   "locations": ["Redmond"],
#   "dates": ["January 2023"],
#   "money": ["$10 billion"]
# }
```

### Invoice Processing

```python
from src.extractors.invoice_extractor import InvoiceExtractor

extractor = InvoiceExtractor()
invoice_text = """
INVOICE #12345
Date: 2024-01-15
Bill To: Acme Corp
Item: Consulting Services - $5,000
Tax: $500
Total: $5,500
"""

invoice_data = extractor.extract(invoice_text)
# Returns structured JSON with all invoice details
```

### Document Summarization

```python
from src.text_extractor import TextExtractor

extractor = TextExtractor()
long_document = "..." # Your long text here

# Short summary
summary = extractor.summarize(long_document, length="short")

# Executive summary with bullet points
exec_summary = extractor.summarize(
    long_document, 
    style="executive",
    format="bullets"
)
```

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_extractors.py
```

## 📊 Performance Tips

1. **Batch Processing**: Process multiple documents in batches to reduce API calls
2. **Caching**: Enable response caching for repeated queries
3. **Model Selection**: Use smaller models for simple tasks, larger for complex analysis
4. **Prompt Optimization**: Fine-tune prompts for your specific use case

## 🔒 Security & Privacy

- Never commit API keys to version control
- Use environment variables for sensitive data
- Consider data privacy when processing sensitive documents
- Implement rate limiting for production use

## 🛠️ Advanced Configuration

```python
from src.text_extractor import TextExtractor

extractor = TextExtractor(
    provider="anthropic",
    model="claude-3-sonnet-20240229",
    temperature=0.1,  # Lower for more deterministic outputs
    max_tokens=2000,
    cache_responses=True,
    timeout=30
)
```

## 📚 API Documentation

See [docs/API.md](docs/API.md) for detailed API documentation.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- OpenAI for GPT models
- Anthropic for Claude models
- The open-source community

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

## 🗺️ Roadmap

- [ ] Add support for local LLMs (Llama, Mistral)
- [ ] Implement batch processing utilities
- [ ] Add web interface for easy testing
- [ ] Support for PDF and image text extraction
- [ ] Multi-language support
- [ ] Fine-tuning examples
