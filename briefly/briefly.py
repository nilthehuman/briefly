"""The main entry point to the briefly text analyzer tool."""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(url):
    """The main entry point.
    Takes an HTTP URL as parameter to fetch and analyze.
    """
    return render_template('index.html')

@app.route('/echo/<input>')
def echo(input):
    return input

