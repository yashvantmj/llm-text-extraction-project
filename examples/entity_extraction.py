"""
Example: Entity Extraction from Text

This example demonstrates how to extract named entities from text using LLMs.
"""

from src.text_extractor import TextExtractor
import json


def main():
    # Initialize the extractor (will use default provider from .env)
    extractor = TextExtractor(provider="openai")

    # Example 1: News article
    print("=" * 60)
    print("Example 1: News Article Entity Extraction")
    print("=" * 60)

    news_text = """
    Apple Inc. CEO Tim Cook announced a groundbreaking partnership with NASA 
    worth $500 million during a press conference in Cupertino, California on 
    March 15, 2024. The collaboration aims to develop advanced AI systems for 
    space exploration. SpaceX founder Elon Musk congratulated both organizations 
    on Twitter, while Microsoft expressed interest in joining the initiative.
    """

    entities = extractor.extract_entities(news_text)
    print("\nExtracted Entities:")
    print(json.dumps(entities, indent=2))

    # Example 2: Business email
    print("\n" + "=" * 60)
    print("Example 2: Business Email Entity Extraction")
    print("=" * 60)

    email_text = """
    Hi John,
    
    Following our meeting at the Google headquarters in Mountain View last Tuesday,
    I wanted to confirm our partnership with Amazon Web Services. The contract 
    worth €2.5 million will be signed by December 31, 2024. Please coordinate 
    with Sarah Johnson from our London office.
    
    Best regards,
    Michael Chen
    VP of Partnerships
    """

    entities = extractor.extract_entities(email_text)
    print("\nExtracted Entities:")
    print(json.dumps(entities, indent=2))

    # Example 3: Custom entity types
    print("\n" + "=" * 60)
    print("Example 3: Custom Entity Types")
    print("=" * 60)

    custom_text = """
    The new iPhone 15 Pro and Samsung Galaxy S24 will be released next quarter.
    Tesla Model 3 sales reached 500,000 units. The PlayStation 5 shortage 
    continues to affect gamers worldwide.
    """

    custom_entities = extractor.extract_entities(
        custom_text, entity_types=["products", "companies", "numbers"]
    )
    print("\nExtracted Entities (Custom Types):")
    print(json.dumps(custom_entities, indent=2))

    # Example 4: Medical text
    print("\n" + "=" * 60)
    print("Example 4: Medical Text Entity Extraction")
    print("=" * 60)

    medical_text = """
    Patient John Doe was admitted to Mayo Clinic on January 10, 2024, 
    complaining of chest pain. Dr. Sarah Williams prescribed aspirin 100mg 
    and scheduled a follow-up for February 1, 2024, at the Rochester facility.
    """

    medical_entities = extractor.extract_entities(
        medical_text,
        entity_types=["people", "organizations", "dates", "medications", "symptoms"],
    )
    print("\nExtracted Entities:")
    print(json.dumps(medical_entities, indent=2))


if __name__ == "__main__":
    main()
