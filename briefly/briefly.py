"""The main entry point to the briefly text analyzer tool."""

from flask import Flask, render_template
from .http import get_html_text
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
    response = None
    if url is not None:
        url = url.replace('^', '/')
        response = get_html_text('http://' + url)
        if is_in_english(response):
            response = strip_common_words(response)
        else:
            response = u'That webpage does not seem to be written in English. \U0001f928'
    return render_template('index.html', url=url, response=response)

