"""The main entry point to the Briefly text analyzer service."""

from flask import Flask, render_template
from .http import get_html_text, get_the_body_only
from .score import gensim_lda, highlight_keywords
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
    keywords_message = None
    full_text, body_text = None, None
    if url is not None:
        url = url.replace('^', '/')
        full_text, body_text = get_html_text('http://' + url)
        if full_text is not None and is_in_english(full_text):
            keywords = gensim_lda(full_text)
            keywords_message = '[ ' + ', '.join(keywords) + ' ]'
            body_text = highlight_keywords(full_text, keywords)
        else:
            body_text = u'That webpage does not seem to be written in English. \U0001f928'
    return render_template('index.html', url=url, keywords=keywords_message, text=body_text)

