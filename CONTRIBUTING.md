# Contributing to LLM Text Extraction

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, etc.)

### Suggesting Features

Feature suggestions are welcome! Please create an issue describing:
- The feature you'd like to see
- Use cases and benefits
- Potential implementation approach

### Code Contributions

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/llm-text-extraction-project.git
   cd llm-text-extraction-project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e ".[dev]"  # Install development dependencies
   ```

4. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

5. **Make your changes**
   - Write clean, documented code
   - Follow existing code style
   - Add tests for new functionality
   - Update documentation as needed

6. **Run tests**
   ```bash
   pytest tests/
   ```

7. **Check code quality**
   ```bash
   black src/ tests/  # Format code
   flake8 src/ tests/  # Check style
   mypy src/           # Type checking
   ```

8. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: your feature description"
   ```

9. **Push and create pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Style

- Follow PEP 8 guidelines
- Use type hints where possible
- Write docstrings for all functions and classes
- Keep functions focused and concise
- Use meaningful variable names

### Example:

```python
def extract_entities(
    text: str, 
    entity_types: Optional[List[str]] = None
) -> Dict[str, List[str]]:
    """
    Extract named entities from text.

    Args:
        text: Input text to extract entities from
        entity_types: List of entity types to extract (optional)

    Returns:
        Dictionary mapping entity types to lists of entities

    Example:
        >>> extractor = TextExtractor()
        >>> entities = extractor.extract_entities("Apple Inc. in Cupertino")
        >>> print(entities)
        {"organizations": ["Apple Inc."], "locations": ["Cupertino"]}
    """
    # Implementation
    pass
```

## Testing Guidelines

- Write tests for all new functionality
- Aim for >80% code coverage
- Use meaningful test names
- Test edge cases and error conditions

### Example test:

```python
def test_extract_entities_with_custom_types():
    """Test entity extraction with custom entity types."""
    extractor = TextExtractor()
    result = extractor.extract_entities(
        "iPhone 15", 
        entity_types=["products"]
    )
    assert "products" in result
    assert "iPhone 15" in result["products"]
```

## Documentation

- Update README.md for significant changes
- Add docstrings to new functions/classes
- Update API.md for API changes
- Include examples in docstrings

## Adding New Extractors

When adding a new specialized extractor:

1. Create new file in `src/extractors/`
2. Inherit from TextExtractor or create standalone class
3. Add comprehensive docstrings
4. Create example in `examples/`
5. Add tests in `tests/`
6. Update documentation

## Pull Request Process

1. Ensure all tests pass
2. Update documentation
3. Add yourself to contributors (if first contribution)
4. Write clear PR description explaining changes
5. Link related issues
6. Wait for review and address feedback

## Questions?

Feel free to open an issue for any questions or clarifications!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
