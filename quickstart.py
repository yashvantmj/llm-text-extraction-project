#!/usr/bin/env python3
"""
Quick Start Demo - LLM Text Extraction

This script provides a quick demonstration of the main features.
Make sure you have set up your .env file with API keys before running.
"""

import os
from dotenv import load_dotenv
from src.text_extractor import TextExtractor

# Load environment variables
load_dotenv()


def check_api_keys():
    """Check if API keys are configured."""
    openai_key = os.getenv("OPENAI_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")

    if not openai_key and not anthropic_key:
        print("❌ ERROR: No API keys found!")
        print("\nPlease:")
        print("1. Copy .env.example to .env")
        print("2. Add your OpenAI or Anthropic API key")
        print("3. Run this script again")
        return False

    if openai_key:
        print("✓ OpenAI API key found")
    if anthropic_key:
        print("✓ Anthropic API key found")

    return True


def demo_entity_extraction(extractor):
    """Demonstrate entity extraction."""
    print("\n" + "=" * 60)
    print("DEMO 1: Entity Extraction")
    print("=" * 60)

    text = """
    Microsoft CEO Satya Nadella announced a $10 billion investment 
    in OpenAI during a press conference in Redmond on January 23, 2023.
    """

    print(f"\nText: {text.strip()}")
    print("\nExtracting entities...")

    try:
        entities = extractor.extract_entities(text)
        print("\n✓ Entities extracted successfully!")
        for entity_type, values in entities.items():
            if values:
                print(f"  {entity_type}: {', '.join(values)}")
    except Exception as e:
        print(f"\n❌ Error: {e}")


def demo_summarization(extractor):
    """Demonstrate text summarization."""
    print("\n" + "=" * 60)
    print("DEMO 2: Text Summarization")
    print("=" * 60)

    text = """
    Artificial intelligence is transforming industries worldwide. From healthcare
    to finance, AI-powered systems are improving efficiency and decision-making.
    Machine learning algorithms analyze vast amounts of data to identify patterns
    and make predictions. Deep learning has enabled breakthroughs in image 
    recognition and natural language processing. However, ethical considerations
    around AI deployment remain important. Privacy concerns, algorithmic bias,
    and job displacement are key challenges that need addressing as AI continues
    to advance.
    """

    print(f"\nOriginal text ({len(text)} characters)")
    print("\nGenerating summary...")

    try:
        summary = extractor.summarize(text, length="short")
        print("\n✓ Summary generated successfully!")
        print(f"\nSummary: {summary}")
    except Exception as e:
        print(f"\n❌ Error: {e}")


def demo_sentiment_analysis(extractor):
    """Demonstrate sentiment analysis."""
    print("\n" + "=" * 60)
    print("DEMO 3: Sentiment Analysis")
    print("=" * 60)

    text = """
    I absolutely loved this product! The quality exceeded my expectations 
    and the customer service was fantastic. Highly recommend to everyone!
    """

    print(f"\nText: {text.strip()}")
    print("\nAnalyzing sentiment...")

    try:
        sentiment = extractor.analyze_sentiment(text)
        print("\n✓ Sentiment analyzed successfully!")
        print(f"  Overall: {sentiment.get('overall_sentiment', 'N/A')}")
        print(f"  Confidence: {sentiment.get('confidence', 'N/A')}")
        if sentiment.get("emotions"):
            print(f"  Emotions: {', '.join(sentiment['emotions'])}")
    except Exception as e:
        print(f"\n❌ Error: {e}")


def main():
    """Run the quick start demo."""
    print("\n" + "=" * 60)
    print("LLM Text Extraction - Quick Start Demo")
    print("=" * 60)

    # Check API keys
    if not check_api_keys():
        return

    # Initialize extractor
    print("\nInitializing text extractor...")
    try:
        extractor = TextExtractor()
        print("✓ Extractor initialized successfully!")
    except Exception as e:
        print(f"❌ Error initializing extractor: {e}")
        return

    # Run demos
    demo_entity_extraction(extractor)
    demo_summarization(extractor)
    demo_sentiment_analysis(extractor)

    # Success message
    print("\n" + "=" * 60)
    print("✓ Demo completed successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Check out the examples/ directory for more detailed use cases")
    print("2. Read docs/API.md for full API documentation")
    print("3. Explore src/extractors/ for specialized extractors")
    print("4. Run tests with: pytest tests/")
    print("\nHappy extracting! 🎉")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
