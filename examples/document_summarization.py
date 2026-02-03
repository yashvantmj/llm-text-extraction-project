"""
Example: Document Summarization

This example demonstrates different summarization styles and lengths.
"""

from src.text_extractor import TextExtractor


def main():
    # Initialize the extractor
    extractor = TextExtractor()

    # Sample long document
    long_document = """
    Artificial Intelligence has revolutionized numerous industries over the past decade,
    transforming how businesses operate and how people interact with technology. Machine
    learning, a subset of AI, enables computers to learn from data without explicit 
    programming. Deep learning, utilizing neural networks with multiple layers, has 
    achieved remarkable breakthroughs in image recognition, natural language processing,
    and game playing.
    
    The healthcare industry has been one of the major beneficiaries of AI technology.
    Medical imaging analysis powered by deep learning can detect diseases like cancer
    with accuracy matching or exceeding human radiologists. AI-driven drug discovery
    platforms are accelerating the development of new medications, reducing the time
    and cost traditionally associated with pharmaceutical research. Predictive analytics
    help hospitals optimize resource allocation and improve patient outcomes.
    
    In the financial sector, AI algorithms analyze vast amounts of market data to identify
    trading opportunities and manage risk. Fraud detection systems use machine learning
    to spot suspicious transactions in real-time, protecting consumers and institutions
    from financial crimes. Chatbots and virtual assistants handle routine customer 
    inquiries, improving service efficiency while reducing operational costs.
    
    The transportation industry is undergoing a transformation with autonomous vehicles.
    Self-driving cars use AI to process sensor data, make split-second decisions, and
    navigate complex traffic scenarios. Companies like Tesla, Waymo, and traditional
    automakers are investing billions in autonomous driving technology, promising to
    reduce accidents, ease traffic congestion, and provide mobility solutions for 
    those unable to drive.
    
    However, the rapid advancement of AI also raises important ethical considerations.
    Concerns about job displacement, algorithmic bias, privacy violations, and the
    potential misuse of AI technology require careful attention from policymakers,
    technologists, and society at large. Ensuring AI development remains aligned with
    human values and benefits all of humanity is one of the defining challenges of
    our time.
    
    Looking ahead, AI will continue to evolve with developments in quantum computing,
    neuromorphic hardware, and advanced algorithms. The integration of AI with other
    emerging technologies like blockchain, IoT, and 5G networks will unlock new
    possibilities and applications we can barely imagine today. As AI becomes more
    sophisticated and ubiquitous, maintaining ethical guidelines and responsible
    development practices will be crucial for creating a future where technology
    serves the common good.
    """

    # Example 1: Short summary
    print("=" * 60)
    print("Example 1: Short Summary")
    print("=" * 60)
    short_summary = extractor.summarize(long_document, length="short")
    print(f"\n{short_summary}\n")

    # Example 2: Medium paragraph summary
    print("=" * 60)
    print("Example 2: Medium Summary (Paragraph)")
    print("=" * 60)
    medium_summary = extractor.summarize(long_document, length="medium")
    print(f"\n{medium_summary}\n")

    # Example 3: Bullet points summary
    print("=" * 60)
    print("Example 3: Bullet Points Summary")
    print("=" * 60)
    bullet_summary = extractor.summarize(
        long_document, length="medium", style="bullets"
    )
    print(f"\n{bullet_summary}\n")

    # Example 4: Executive summary
    print("=" * 60)
    print("Example 4: Executive Summary")
    print("=" * 60)
    exec_summary = extractor.summarize(long_document, style="executive")
    print(f"\n{exec_summary}\n")

    # Example 5: Focused summary
    print("=" * 60)
    print("Example 5: Summary Focused on Healthcare")
    print("=" * 60)
    focused_summary = extractor.summarize(
        long_document, length="medium", focus="healthcare applications and benefits"
    )
    print(f"\n{focused_summary}\n")

    # Example 6: Long detailed summary
    print("=" * 60)
    print("Example 6: Long Detailed Summary")
    print("=" * 60)
    long_summary = extractor.summarize(long_document, length="long")
    print(f"\n{long_summary}\n")


if __name__ == "__main__":
    main()
