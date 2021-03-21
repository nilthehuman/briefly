"""The core topic identification model. Contains functions to calculate the relative score
of each distinct uncommon word in the English text input to help identify the topic."""

from nltk.tokenize import sent_tokenize, word_tokenize

get_sentences = sent_tokenize

def bag_of_words(string):
    """Count the number of times each distinct word occurs.

    This is the dumbest possible algorithm, and requires no parsing at all.
    It merely counts the number of times each distinct word is found in the
    input, regardless of position or syntax."""
    pass

