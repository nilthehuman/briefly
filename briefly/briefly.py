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
@app.route('/briefly/<url>')
def index(url=None):
    """The main entry point.
    Takes an HTTP URL as parameter to fetch and analyze.
    """
    response = None
    if url is not None:
        url = url.replace('^', '/')
        response = get_html_body('http://' + url)
    return render_template('index.html', url=url, response=response)

