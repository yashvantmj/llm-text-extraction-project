"""
Example: Comprehensive Text Analysis Pipeline

This example demonstrates a complete text analysis workflow combining
multiple extraction and analysis techniques.
"""

from src.text_extractor import TextExtractor
from src.utils.text_utils import (
    calculate_readability_score,
    extract_emails,
    extract_phone_numbers,
    extract_urls,
    find_keywords,
)
import json


def analyze_document(text: str, extractor: TextExtractor) -> dict:
    """
    Perform comprehensive analysis on a document.

    Args:
        text: Document text to analyze
        extractor: TextExtractor instance

    Returns:
        Dictionary with all analysis results
    """
    results = {}

    print("Analyzing document...")

    # 1. Extract entities
    print("  - Extracting entities...")
    results["entities"] = extractor.extract_entities(text)

    # 2. Generate summary
    print("  - Generating summary...")
    results["summary"] = extractor.summarize(text, length="medium")

    # 3. Analyze sentiment
    print("  - Analyzing sentiment...")
    results["sentiment"] = extractor.analyze_sentiment(text)

    # 4. Calculate readability
    print("  - Calculating readability...")
    results["readability"] = calculate_readability_score(text)

    # 5. Extract contact information
    print("  - Extracting contact information...")
    results["contacts"] = {
        "emails": extract_emails(text),
        "phones": extract_phone_numbers(text),
        "urls": extract_urls(text),
    }

    # 6. Find keywords
    print("  - Finding keywords...")
    results["keywords"] = find_keywords(text, top_n=10)

    print("✓ Analysis complete!\n")
    return results


def main():
    # Initialize extractor
    extractor = TextExtractor()

    # Example document: Press release
    document = """
    FOR IMMEDIATE RELEASE

    TechVision Inc. Announces Breakthrough in AI Technology

    San Francisco, CA - January 15, 2024 - TechVision Inc. (NASDAQ: TVAI), a 
    leading innovator in artificial intelligence solutions, today announced the 
    launch of its revolutionary AI-powered analytics platform, InsightEngine 3.0. 
    This groundbreaking technology represents a major leap forward in machine 
    learning capabilities and data processing efficiency.

    "We are thrilled to introduce InsightEngine 3.0 to the market," said Sarah 
    Johnson, CEO of TechVision Inc. "This platform will transform how businesses 
    analyze and leverage their data, providing unprecedented insights and driving 
    better decision-making across all industries."

    Key features of InsightEngine 3.0 include:

    - 10x faster data processing compared to previous versions
    - Advanced natural language processing with 98% accuracy
    - Real-time predictive analytics powered by deep learning
    - Seamless integration with existing enterprise systems
    - Enhanced security protocols meeting SOC 2 Type II compliance

    The platform has already been adopted by major corporations including Global 
    Finance Corp, MediCare Systems, and RetailMax International, with impressive 
    results. Beta testing showed an average 45% improvement in operational 
    efficiency and 30% cost reduction in data analysis workflows.

    "InsightEngine 3.0 has completely transformed our data analytics capabilities," 
    said Michael Chen, Chief Data Officer at Global Finance Corp. "The insights 
    we're gaining are helping us make faster, more informed decisions that directly 
    impact our bottom line."

    TechVision Inc. will be showcasing InsightEngine 3.0 at the upcoming TechWorld 
    Conference in New York City from March 10-12, 2024. The company is offering 
    free trials to qualified enterprises through the end of Q1 2024.

    Pricing starts at $50,000 per year for the basic tier, with custom enterprise 
    solutions available. For more information, visit www.techvision.com/insightengine 
    or contact our sales team at sales@techvision.com or call +1-800-TECH-AI1.

    About TechVision Inc.
    Founded in 2015 and headquartered in San Francisco, TechVision Inc. is a 
    pioneering force in artificial intelligence and machine learning solutions. 
    The company serves over 500 enterprise clients worldwide and has been recognized 
    as a leader in the Gartner Magic Quadrant for AI platforms for three consecutive 
    years.

    Media Contact:
    Jennifer Williams
    Director of Communications
    TechVision Inc.
    jennifer.williams@techvision.com
    +1-415-555-0123

    ###
    """

    print("=" * 60)
    print("Comprehensive Document Analysis Example")
    print("=" * 60)
    print(f"\nDocument Length: {len(document)} characters")
    print(f"Word Count: {len(document.split())} words\n")

    # Perform comprehensive analysis
    results = analyze_document(document, extractor)

    # Display results
    print("=" * 60)
    print("ANALYSIS RESULTS")
    print("=" * 60)

    # Entities
    print("\n1. EXTRACTED ENTITIES")
    print("-" * 40)
    for entity_type, values in results["entities"].items():
        if values:
            print(f"{entity_type.upper()}:")
            for value in values:
                print(f"  • {value}")

    # Summary
    print("\n2. DOCUMENT SUMMARY")
    print("-" * 40)
    print(results["summary"])

    # Sentiment
    print("\n3. SENTIMENT ANALYSIS")
    print("-" * 40)
    sentiment = results["sentiment"]
    print(f"Overall Sentiment: {sentiment.get('overall_sentiment', 'N/A')}")
    print(f"Confidence: {sentiment.get('confidence', 'N/A')}")
    if sentiment.get("emotions"):
        print(f"Detected Emotions: {', '.join(sentiment['emotions'])}")

    # Readability
    print("\n4. READABILITY METRICS")
    print("-" * 40)
    readability = results["readability"]
    print(f"Word Count: {readability['word_count']}")
    print(f"Sentence Count: {readability['sentence_count']}")
    print(f"Avg Words/Sentence: {readability['avg_words_per_sentence']}")
    print(f"Reading Level: {readability['reading_level']}")

    # Contact Information
    print("\n5. CONTACT INFORMATION")
    print("-" * 40)
    contacts = results["contacts"]
    if contacts["emails"]:
        print(f"Emails: {', '.join(contacts['emails'])}")
    if contacts["phones"]:
        print(f"Phone Numbers: {', '.join(contacts['phones'])}")
    if contacts["urls"]:
        print(f"URLs: {', '.join(contacts['urls'])}")

    # Keywords
    print("\n6. TOP KEYWORDS")
    print("-" * 40)
    print(", ".join(results["keywords"]))

    # Export results
    print("\n" + "=" * 60)
    print("Exporting results to JSON...")
    with open("/home/claude/analysis_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("✓ Results saved to analysis_results.json")

    print("\n" + "=" * 60)
    print("Analysis Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
