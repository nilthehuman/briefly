"""This module lists the ~100 most common English words that carry little topical information.

Lemmata from en.wikipedia.org/wiki/Most_common_words_in_English, inflected forms added by hand.
Items sorted by category and meaning to make the whole list more readable. Order does not matter.

The following items were removed: 'day', 'first', 'good', 'new', 'only', 'people', 'time', 'two',
                                  'way', 'work', 'year'.
The following new items were added: 'before', 'down, 'few', 'here', 'many', 'those', 'though',
                                    'under' ,'where', 'whom', 'whose', 'why'.
"""

COMMON_ENGLISH_NON_VERBS = [
    # articles
    'the', 'a', 'an',
    # demonstratives and 'other' (a similar determiner)
    'this', 'that', 'these', 'those', 'other',
    # prepositions
    'from', 'to', 'of', 'for', 'in', 'into', 'out', 'on', 'up', 'down', 'at', 'after', 'before',
    'over', 'under', 'as', 'by', 'with', 'because', 'about',
    # interrogatives
    'what', 'who', 'whom', 'whose', 'which', 'when', 'where', 'how', 'why',
    # conjunctions
    'and', 'or', 'so', 'but', 'though', 'if', 'then', 'than',
    # adverbs
    'no', 'not', 'n\'t', 'now', 'here', 'there', 'also', 'just', 'back', 'even', 'very', 'well',
    # numerals and quantifiers
    'one', 'all', 'any', 'most', 'some', 'many', 'few',
    # personal and possessive pronouns
    'I', 'me', 'my', 'mine', 'you', 'your', 'yours',
    'it', 'its', 'he', 'him', 'his', 'she', 'her', 'hers',
    'we', 'us', 'our', 'ours', 'they', 'them', 'their', 'theirs'
]

COMMON_ENGLISH_VERBS = [
    'be', 'am', 'are', 'is', 'was', 'were', 'being', 'been',
    'have', 'has', 'having', 'had',
    'do', 'does', 'doing', 'did', 'done',
    'will', 'would',
    'get', 'gets', 'getting', 'got', 'gotten',
    'come', 'comes', 'coming', 'came',
    'go', 'goes', 'going', 'went', 'gone',
    'say', 'says', 'saying', 'said',
    'make', 'makes', 'making', 'made',
    'can', 'could', 'able',
    'like', 'likes', 'liking', 'liked',
    'know', 'knows', 'knowing', 'knew', 'known',
    'take', 'takes', 'taking', 'took', 'taken',
    'see', 'sees', 'seeing', 'saw', 'seen',
    'look', 'looks', 'looking', 'looked',
    'think', 'thinks', 'thinking', 'thought',
    'use', 'uses', 'using', 'used',
    'want', 'wants', 'wanting', 'wanted',
    'give', 'gives', 'giving', 'gave', 'given'
]

# Ensure no duplicates
assert len(list(set(COMMON_ENGLISH_NON_VERBS))) == len(COMMON_ENGLISH_NON_VERBS)
assert len(list(set(COMMON_ENGLISH_VERBS))) == len(COMMON_ENGLISH_VERBS)

COMMON_ENGLISH_WORDS = COMMON_ENGLISH_NON_VERBS + COMMON_ENGLISH_VERBS
