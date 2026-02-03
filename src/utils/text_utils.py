"""
Text processing utilities.
"""

import re
from typing import List, Dict, Any


def clean_text(text: str) -> str:
    """
    Clean and normalize text.

    Args:
        text: Input text to clean

    Returns:
        Cleaned text
    """
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)
    # Remove leading/trailing whitespace
    text = text.strip()
    return text


def split_into_chunks(text: str, max_length: int = 4000, overlap: int = 200) -> List[str]:
    """
    Split text into chunks for processing.

    Args:
        text: Text to split
        max_length: Maximum length of each chunk
        overlap: Number of characters to overlap between chunks

    Returns:
        List of text chunks
    """
    if len(text) <= max_length:
        return [text]

    chunks = []
    start = 0

    while start < len(text):
        end = start + max_length
        chunk = text[start:end]

        # Try to break at sentence boundary
        if end < len(text):
            last_period = chunk.rfind(".")
            last_newline = chunk.rfind("\n")
            break_point = max(last_period, last_newline)

            if break_point > 0:
                end = start + break_point + 1
                chunk = text[start:end]

        chunks.append(chunk)
        start = end - overlap

    return chunks


def extract_emails(text: str) -> List[str]:
    """
    Extract email addresses from text.

    Args:
        text: Text to extract emails from

    Returns:
        List of email addresses
    """
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return re.findall(email_pattern, text)


def extract_phone_numbers(text: str) -> List[str]:
    """
    Extract phone numbers from text.

    Args:
        text: Text to extract phone numbers from

    Returns:
        List of phone numbers
    """
    # Match various phone number formats
    patterns = [
        r"\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",  # International
        r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",  # US format
    ]

    phone_numbers = []
    for pattern in patterns:
        phone_numbers.extend(re.findall(pattern, text))

    return list(set(phone_numbers))  # Remove duplicates


def extract_urls(text: str) -> List[str]:
    """
    Extract URLs from text.

    Args:
        text: Text to extract URLs from

    Returns:
        List of URLs
    """
    url_pattern = r"https?://[^\s<>\"{}|\\^`\[\]]+"
    return re.findall(url_pattern, text)


def calculate_readability_score(text: str) -> Dict[str, Any]:
    """
    Calculate basic readability metrics.

    Args:
        text: Text to analyze

    Returns:
        Dictionary with readability metrics
    """
    # Count sentences
    sentences = re.split(r"[.!?]+", text)
    sentence_count = len([s for s in sentences if s.strip()])

    # Count words
    words = text.split()
    word_count = len(words)

    # Count syllables (simplified)
    syllable_count = sum(count_syllables(word) for word in words)

    # Calculate metrics
    avg_words_per_sentence = word_count / max(sentence_count, 1)
    avg_syllables_per_word = syllable_count / max(word_count, 1)

    # Flesch Reading Ease (simplified)
    if sentence_count > 0 and word_count > 0:
        reading_ease = (
            206.835
            - 1.015 * avg_words_per_sentence
            - 84.6 * avg_syllables_per_word
        )
    else:
        reading_ease = 0

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "avg_words_per_sentence": round(avg_words_per_sentence, 2),
        "avg_syllables_per_word": round(avg_syllables_per_word, 2),
        "reading_ease": round(reading_ease, 2),
        "reading_level": get_reading_level(reading_ease),
    }


def count_syllables(word: str) -> int:
    """
    Count syllables in a word (simplified).

    Args:
        word: Word to count syllables in

    Returns:
        Number of syllables
    """
    word = word.lower()
    vowels = "aeiouy"
    syllable_count = 0
    previous_was_vowel = False

    for char in word:
        is_vowel = char in vowels
        if is_vowel and not previous_was_vowel:
            syllable_count += 1
        previous_was_vowel = is_vowel

    # Adjust for silent e
    if word.endswith("e"):
        syllable_count -= 1

    # Ensure at least one syllable
    return max(syllable_count, 1)


def get_reading_level(reading_ease: float) -> str:
    """
    Get reading level description from reading ease score.

    Args:
        reading_ease: Flesch Reading Ease score

    Returns:
        Reading level description
    """
    if reading_ease >= 90:
        return "Very Easy (5th grade)"
    elif reading_ease >= 80:
        return "Easy (6th grade)"
    elif reading_ease >= 70:
        return "Fairly Easy (7th grade)"
    elif reading_ease >= 60:
        return "Standard (8th-9th grade)"
    elif reading_ease >= 50:
        return "Fairly Difficult (10th-12th grade)"
    elif reading_ease >= 30:
        return "Difficult (College)"
    else:
        return "Very Difficult (College graduate)"


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length.

    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add if truncated

    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text

    return text[: max_length - len(suffix)].strip() + suffix


def remove_special_characters(text: str, keep_spaces: bool = True) -> str:
    """
    Remove special characters from text.

    Args:
        text: Text to process
        keep_spaces: Whether to keep spaces

    Returns:
        Text with special characters removed
    """
    if keep_spaces:
        return re.sub(r"[^a-zA-Z0-9\s]", "", text)
    else:
        return re.sub(r"[^a-zA-Z0-9]", "", text)


def find_keywords(text: str, top_n: int = 10) -> List[str]:
    """
    Extract top keywords from text (simple frequency-based).

    Args:
        text: Text to extract keywords from
        top_n: Number of top keywords to return

    Returns:
        List of top keywords
    """
    # Remove common stop words
    stop_words = {
        "the",
        "a",
        "an",
        "and",
        "or",
        "but",
        "in",
        "on",
        "at",
        "to",
        "for",
        "of",
        "with",
        "by",
        "from",
        "as",
        "is",
        "was",
        "are",
        "been",
        "be",
        "have",
        "has",
        "had",
        "do",
        "does",
        "did",
        "will",
        "would",
        "should",
        "could",
        "may",
        "might",
        "must",
        "can",
        "this",
        "that",
        "these",
        "those",
        "i",
        "you",
        "he",
        "she",
        "it",
        "we",
        "they",
        "what",
        "which",
        "who",
        "when",
        "where",
        "why",
        "how",
    }

    # Tokenize and clean
    words = text.lower().split()
    words = [re.sub(r"[^a-z]", "", word) for word in words]
    words = [word for word in words if word and word not in stop_words and len(word) > 2]

    # Count frequencies
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # Get top N
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, _ in sorted_words[:top_n]]
