"""The core topic identification model. Contains functions to calculate the relative score
of each distinct uncommon word in the English text input to help identify the topic."""

from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
from gensim.corpora import Dictionary
from gensim.models.ldamodel import LdaModel
from .tokenize import get_words
from .verify_english import strip_common_words, strip_single_letter_words

get_sentences = sent_tokenize

def gensim_lda(string):
    """Latent Dirichlet Allocation, a popular method, courtesy of the Gensim library."""
    words = map(lambda w: w.lower(), get_words(string))
    words = strip_common_words(strip_single_letter_words(words))
    lemmata = [w for w in map(wordnet.morphy, words) if w is not None]
    dictionary = Dictionary([lemmata])
    bow = dictionary.doc2bow(lemmata)
    lda_model = LdaModel([bow], num_topics=5, id2word=dictionary)
    # print_topics() spits out a list of pairs whose second elements are strings
    # with the main topic keywords buried in them, e.g.:
    # [(0, '0.148*"cats"'), (1, '0.225*"mice"'), (2, '0.150*"dogs"')]
    topic_vector = lda_model.print_topics(num_words=2)
    topics = [t.split('"')[1] for (_, t) in topic_vector] + [t.split('"')[3] for (_, t) in topic_vector]
    best_topics = list(t for t,_ in Counter(topics).most_common()[0:3])
    return best_topics

def bag_of_words(string):
    """Count the number of times each distinct word occurs.

    This is the dumbest possible algorithm, and requires no parsing at all.
    It merely counts the number of times each distinct word is found in the
    input, regardless of position or syntax."""
    # TODO
    pass

