"""A few helper functions to determine if a given text is written in English."""

from itertools import chain

from .common_words import COMMON_ENGLISH_NON_VERBS, COMMON_ENGLISH_WORDS
from .tokenize import get_words

ENGLISH_ALPHABET = [chr(x) for x in chain(range(ord('A'), ord('Z')+1), range(ord('a'), ord('z')+1))]

ARABIC_NUMERALS = [str(x) for x in range(0, 10)]

WHITESPACE = [' ', '\n', '\r', '\t']

PUNCTUATION = [',', '(', ')', '[', ']', '"', '`', '\'', ':', ';', '.', '!', '?', '_', '-', '*']

ENGLISH_CHARSET = ENGLISH_ALPHABET + ARABIC_NUMERALS + WHITESPACE + PUNCTUATION

def non_english_characters(string):
    """Remove all valid Latin characters and symbols from a string."""
    to_remove = str.maketrans(dict.fromkeys(ENGLISH_CHARSET))
    return string.translate(to_remove)

def prevalence_of_english_characters(string):
    """Determine the ratio of valid Latin characters and symbols in a string (between 0 and 1)."""
    remaining_char_count = len(non_english_characters(string))
    total_char_count = len(string)
    return 1 - remaining_char_count / total_char_count

def strip_common_non_verbs(tokens):
    """Remove the most common non-verb words from a list of tokens."""
    return list(filter(lambda x: x.lower() not in COMMON_ENGLISH_NON_VERBS, tokens))

def strip_common_words(tokens):
    """Remove the most common English words from a list of tokens."""
    return list(filter(lambda x: x.lower() not in COMMON_ENGLISH_WORDS, tokens))

def strip_single_letter_words(tokens):
    """Remove all tokens with just one letter in them."""
    return list(x for x in tokens if 1 < len(x))

def prevalence_of_common_words(tokens):
    """Determine the ratio of common words in a list of tokens (between 0 and 1)."""
    remaining_token_count = len(strip_common_words(tokens))
    total_token_count = len(tokens)
    return 1 - remaining_token_count / total_token_count

ENGLISH_CHARACTER_LIMIT = 0.9
ENGLISH_WORDS_LIMIT = 0.2

def is_in_english(string):
    """Find out if the given string is writter in English."""
    tokens = get_words(string)
    return (ENGLISH_CHARACTER_LIMIT < prevalence_of_english_characters(string)
            and ENGLISH_WORDS_LIMIT < prevalence_of_common_words(tokens))
