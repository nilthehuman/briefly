"""The main entry point to the Briefly text analyzer service."""

from flask import Flask, render_template

from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

from .http import get_html_text
from .score import gensim_lda
from .tokenize import get_words
from .verify_english import strip_common_words, is_in_english

app = Flask(__name__)

@app.route('/')
def nothing():
    return "Nothing to see here, move along."

@app.route('/echo/<input>')
def echo(input):
    return input

@app.route('/briefly/')
@app.route('/briefly/<url>')
def index(url=None):
    """The main entry point.
    Takes an HTTP URL as parameter to fetch and analyze.
    """
    text = None
    english = None
    keywords_message = None
    body_text = None
    if url is not None:
        url = url.replace('^', '/')
        full_text, body_text = get_html_text('http://' + url)
        if full_text is not None:
            english = is_in_english(full_text)
            if english:
                keywords = gensim_lda(full_text)
                keywords_message = make_keywords_message(keywords)
                body_text = highlight_keywords(body_text, keywords)
    return render_template('index.html', url=url, english=english, keywords=keywords_message, text=body_text)

def make_keywords_message(keywords):
    """Colorize keywords and string them together."""
    keywords_message = ('[ ' +
                           (f'<span class=\'hottest\'>{keywords[0]}</span>' if 0 < len(keywords) else '') +
                           (f', <span class=\'hotter\'>{keywords[1]}</span>' if 1 < len(keywords) else '') +
                           (f', <span class=\'hot\'>{keywords[2]}</span>' if 2 < len(keywords) else '') +
                        ' ]')
    return keywords_message

def highlight_keywords(body_text, keywords):
    """Generate HTML with keywords marked in color."""
    keylemmata = list(map(wordnet.murphy, keywords))
    def colorize(word):
        nonlocal keylemmata
        lemma = wordnet.murphy(word)
        if not lemma:
            return word
        if lemma == keylemmata[0]:
            return f'<span class=\'hottest\'>{word}</span>'
        elif lemma == keylemmata[1]:
            return f'<span class=\'hotter\'>{word}</span>'
        elif lemma == keylemmata[2]:
            return f'<span class=\'hot\'>{word}</span>'
        else:
            return word
    color_text = ' '.join(colorize(word) for word in word_tokenize(body_text))
    return color_text
