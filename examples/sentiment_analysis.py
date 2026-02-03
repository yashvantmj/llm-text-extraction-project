"""
Example: Sentiment Analysis

This example demonstrates how to analyze sentiment and emotional tone of text.
"""

from src.text_extractor import TextExtractor
import json


def main():
    # Initialize the extractor
    extractor = TextExtractor()

    # Example 1: Product review (positive)
    print("=" * 60)
    print("Example 1: Product Review (Positive)")
    print("=" * 60)

    review1 = """
    I absolutely love this product! The quality exceeded my expectations and 
    the customer service was fantastic. Delivery was quick and the packaging 
    was excellent. I've already recommended it to all my friends and family. 
    This is definitely my best purchase this year. Five stars all the way!
    """

    sentiment1 = extractor.analyze_sentiment(review1)
    print("\nSentiment Analysis:")
    print(json.dumps(sentiment1, indent=2))

    # Example 2: Product review (negative)
    print("\n" + "=" * 60)
    print("Example 2: Product Review (Negative)")
    print("=" * 60)

    review2 = """
    Very disappointed with this purchase. The product broke after just one week 
    of normal use. Customer support was unhelpful and refused to provide a refund. 
    The description was misleading and the quality is terrible. Save your money 
    and avoid this product at all costs. Extremely frustrated with this experience.
    """

    sentiment2 = extractor.analyze_sentiment(review2)
    print("\nSentiment Analysis:")
    print(json.dumps(sentiment2, indent=2))

    # Example 3: News article (neutral)
    print("\n" + "=" * 60)
    print("Example 3: News Article (Neutral)")
    print("=" * 60)

    news = """
    The Federal Reserve announced today that interest rates will remain unchanged 
    at 5.25%. The decision was made following a review of current economic indicators 
    including inflation rates, employment figures, and GDP growth. Economists had 
    predicted this outcome based on recent economic data. The next meeting is 
    scheduled for June.
    """

    sentiment3 = extractor.analyze_sentiment(news)
    print("\nSentiment Analysis:")
    print(json.dumps(sentiment3, indent=2))

    # Example 4: Social media post (mixed)
    print("\n" + "=" * 60)
    print("Example 4: Social Media Post (Mixed)")
    print("=" * 60)

    social_post = """
    Had a bittersweet day today. Finally got the promotion I've been working 
    towards for years - I'm thrilled! But I'll really miss working with my 
    current team. Change is exciting but also a bit scary. Grateful for this 
    opportunity but nervous about the new responsibilities. Here's to new 
    beginnings! 🎉😊😬
    """

    sentiment4 = extractor.analyze_sentiment(social_post)
    print("\nSentiment Analysis:")
    print(json.dumps(sentiment4, indent=2))

    # Example 5: Customer feedback
    print("\n" + "=" * 60)
    print("Example 5: Customer Feedback")
    print("=" * 60)

    feedback = """
    The software has some great features and the interface is intuitive. However, 
    it crashes frequently and the mobile app needs improvement. Support team is 
    responsive but resolution times are too long. Overall, it's decent but there's 
    definitely room for improvement. I might recommend it with reservations.
    """

    sentiment5 = extractor.analyze_sentiment(feedback)
    print("\nSentiment Analysis:")
    print(json.dumps(sentiment5, indent=2))

    # Example 6: Email communication
    print("\n" + "=" * 60)
    print("Example 6: Professional Email")
    print("=" * 60)

    email = """
    Dear Team,
    
    I wanted to express my sincere appreciation for all the hard work you've 
    put into this project. Despite the challenges we faced, everyone showed 
    incredible dedication and professionalism. The results speak for themselves - 
    we exceeded our targets and the client is extremely satisfied. I'm proud 
    to work with such a talented group of individuals. Thank you all!
    
    Best regards,
    Manager
    """

    sentiment6 = extractor.analyze_sentiment(email)
    print("\nSentiment Analysis:")
    print(json.dumps(sentiment6, indent=2))


if __name__ == "__main__":
    main()
