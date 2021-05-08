"""The main entry point to the briefly text analyzer tool."""

from flask import Flask, render_template
from .http import get_html_body

app = Flask(__name__)

@app.route('/')
def nothing():
    return "Nothing to see here, move along."

@app.route('/echo/<input>')
def echo(input):
    return input

@app.route('/briefly/')
@app.route('/briefly/<input>')
def index(url=None):
    """The main entry point.
    Takes an HTTP URL as parameter to fetch and analyze.
    """
    response = None
    if url is not None:
        response = get_html_body(url) is not None
    return render_template('index.html', url=url, response=response)

