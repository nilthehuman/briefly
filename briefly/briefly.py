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
    if url is not None:
        url = url.replace('^', '/')
        text = get_html_text('http://' + url)
        if is_in_english(text):
            keywords = gensim_lda(text)
            keyword_message = '[ ' + ', '.join(gensim_lda(text)) + ' ]'
            text = highlight_keywords(text, keywords)
        else:
            text = u'That webpage does not seem to be written in English. \U0001f928'
    return render_template('index.html', url=url, keywords=keyword_message, text=get_the_body_only(text))

