# API Documentation

## TextExtractor

Main class for text extraction and understanding using LLMs.

### Initialization

```python
from src.text_extractor import TextExtractor

extractor = TextExtractor(
    provider="openai",           # or "anthropic"
    api_key="your-api-key",      # optional, uses env var if not provided
    model="gpt-4-turbo-preview", # optional, uses default if not provided
    temperature=0.1,             # 0.0 to 1.0, lower = more deterministic
    max_tokens=2000              # maximum tokens in response
)
```

### Methods

#### extract_entities()

Extract named entities from text.

```python
entities = extractor.extract_entities(
    text="Your text here",
    entity_types=["people", "organizations", "locations", "dates", "money"]
)

# Returns:
# {
#     "people": ["Name1", "Name2"],
#     "organizations": ["Org1"],
#     "locations": ["Place1"],
#     "dates": ["Date1"],
#     "money": ["$100"]
# }
```

**Parameters:**
- `text` (str): Input text to extract entities from
- `entity_types` (List[str], optional): List of entity types to extract

**Returns:** Dictionary mapping entity types to lists of entities

---

#### summarize()

Summarize a document with configurable length and style.

```python
summary = extractor.summarize(
    text="Your long text here",
    length="medium",        # "short", "medium", or "long"
    style="paragraph",      # "paragraph", "bullets", or "executive"
    focus="key topics"      # optional focus area
)
```

**Parameters:**
- `text` (str): Text to summarize
- `length` (str): "short" (2-3 sentences), "medium" (1 paragraph), or "long" (2-3 paragraphs)
- `style` (str): Output style - "paragraph", "bullets", or "executive"
- `focus` (str, optional): Specific focus area for the summary

**Returns:** Summary text as string

---

#### analyze_sentiment()

Analyze sentiment and emotional tone of text.

```python
sentiment = extractor.analyze_sentiment(text="Your text here")

# Returns:
# {
#     "overall_sentiment": "positive",
#     "confidence": 0.9,
#     "emotions": ["joy", "excitement"],
#     "key_phrases": ["love this", "amazing"],
#     "reasoning": "Explanation of the sentiment"
# }
```

**Parameters:**
- `text` (str): Text to analyze

**Returns:** Dictionary with sentiment analysis results

---

#### extract_structured_data()

Extract structured data based on a provided schema.

```python
schema = {
    "title": "string",
    "author": "string",
    "date": "string",
    "items": ["array of strings"]
}

data = extractor.extract_structured_data(
    text="Your text here",
    schema=schema
)
```

**Parameters:**
- `text` (str): Text to extract data from
- `schema` (Dict): JSON schema describing desired output structure

**Returns:** Dictionary with extracted data matching the schema

---

#### classify_text()

Classify text into predefined categories.

```python
# Single label classification
category = extractor.classify_text(
    text="Your text here",
    categories=["sports", "technology", "politics"],
    multi_label=False
)

# Multi-label classification
categories = extractor.classify_text(
    text="Your text here",
    categories=["sports", "technology", "politics"],
    multi_label=True
)
```

**Parameters:**
- `text` (str): Text to classify
- `categories` (List[str]): List of possible categories
- `multi_label` (bool): Whether to allow multiple categories

**Returns:** Single category (str) or list of categories (List[str])

---

#### extract_key_information()

Extract specific types of information from text.

```python
info = extractor.extract_key_information(
    text="Your text here",
    information_types=["main_idea", "key_points", "action_items"]
)

# Returns:
# {
#     "main_idea": "...",
#     "key_points": ["...", "..."],
#     "action_items": ["...", "..."]
# }
```

**Parameters:**
- `text` (str): Text to extract from
- `information_types` (List[str]): Types of information to extract

**Returns:** Dictionary with extracted information

---

## InvoiceExtractor

Specialized extractor for invoices and receipts.

### Initialization

```python
from src.extractors.invoice_extractor import InvoiceExtractor

extractor = InvoiceExtractor(
    provider="openai",     # optional
    api_key="your-api-key" # optional
)
```

### Methods

#### extract()

Extract all invoice data.

```python
invoice_data = extractor.extract(invoice_text)

# Returns comprehensive invoice data including:
# - invoice_number, dates
# - vendor and customer information
# - line items
# - totals, tax, payment terms
```

**Parameters:**
- `invoice_text` (str): Raw invoice text

**Returns:** Dictionary with complete invoice data

---

#### extract_line_items()

Extract only line items from invoice.

```python
items = extractor.extract_line_items(invoice_text)

# Returns:
# [
#     {
#         "description": "Item name",
#         "quantity": 2,
#         "unit_price": 50.00,
#         "total": 100.00
#     }
# ]
```

---

#### validate_invoice()

Validate extracted invoice data.

```python
validation = extractor.validate_invoice(invoice_data)

# Returns:
# {
#     "valid": True,
#     "warnings": ["warning messages"],
#     "errors": ["error messages"]
# }
```

---

#### extract_and_validate()

Extract and validate in one step.

```python
result = extractor.extract_and_validate(invoice_text)

# Returns:
# {
#     "data": {...},
#     "validation": {...}
# }
```

---

## ResumeExtractor

Specialized extractor for resumes and CVs.

### Initialization

```python
from src.extractors.resume_extractor import ResumeExtractor

extractor = ResumeExtractor(
    provider="openai",     # optional
    api_key="your-api-key" # optional
)
```

### Methods

#### extract()

Extract all resume data.

```python
resume_data = extractor.extract(resume_text)

# Returns comprehensive resume data including:
# - personal_info
# - work_experience
# - education
# - skills
# - certifications
# - projects
```

**Parameters:**
- `resume_text` (str): Raw resume text

**Returns:** Dictionary with complete resume data

---

#### extract_contact_info()

Extract only contact information.

```python
contact = extractor.extract_contact_info(resume_text)

# Returns:
# {
#     "name": "...",
#     "email": "...",
#     "phone": "...",
#     "location": "...",
#     "linkedin": "...",
#     "github": "..."
# }
```

---

#### extract_skills()

Extract only skills, categorized by type.

```python
skills = extractor.extract_skills(resume_text)

# Returns:
# {
#     "technical": ["Python", "JavaScript"],
#     "languages": ["English", "Spanish"],
#     "tools": ["Git", "Docker"],
#     "soft_skills": ["Leadership", "Communication"]
# }
```

---

#### match_job_description()

Analyze how well resume matches a job description.

```python
match = extractor.match_job_description(resume_text, job_description)

# Returns:
# {
#     "match_score": 85,
#     "matching_skills": [...],
#     "missing_skills": [...],
#     "relevant_experience": [...],
#     "strengths": [...],
#     "gaps": [...],
#     "recommendations": [...],
#     "summary": "..."
# }
```

---

#### generate_summary()

Generate professional summary from resume data.

```python
summary = extractor.generate_summary(resume_data)
# Returns: "Professional summary text..."
```

---

## Error Handling

All methods may raise exceptions. Wrap calls in try-except:

```python
try:
    result = extractor.extract_entities(text)
except Exception as e:
    print(f"Error: {e}")
```

Common errors:
- `ValueError`: Invalid parameters or configuration
- API errors: Network issues, rate limits, invalid API keys
- JSON parsing errors: Malformed responses from LLM

---

## Best Practices

1. **Use appropriate temperature**: Lower (0.1-0.3) for factual extraction, higher (0.5-0.8) for creative tasks
2. **Adjust max_tokens**: Increase for longer documents or detailed responses
3. **Cache responses**: For repeated queries, implement caching to reduce API calls
4. **Handle errors gracefully**: Always implement error handling
5. **Validate outputs**: Check extracted data for completeness and accuracy
6. **Use specific prompts**: More specific instructions yield better results
7. **Batch processing**: Process multiple documents together when possible

---

## Rate Limits & Costs

Be aware of provider rate limits and costs:

- **OpenAI**: Check your plan limits at platform.openai.com
- **Anthropic**: Check your plan limits at console.anthropic.com

Implement rate limiting in production:

```python
from time import sleep

for document in documents:
    result = extractor.extract(document)
    sleep(1)  # Add delay between requests
```
