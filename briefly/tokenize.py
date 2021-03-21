"""Helper functions for breaking up text into sentences and words."""

from nltk.tokenize import sent_tokenize, word_tokenize

get_sentences = sent_tokenize

def get_words(string):
    """Extract all words from a string."""
    tokens = word_tokenize(string)
    words = list(filter(lambda x: any(map(str.isalnum, x)), tokens))
    return words

def oxford_join(words):
    """Concatenate words with commas and a final 'and' between."""
    assert len(words) > 0
    if len(words) == 1:
        return words[0]
    if len(words) == 2:
        return words[0] + ' and ' + words[1]
    return ' '.join(map(lambda x: x + ',', words[0:-1])) + ' and ' + words[-1]
