"""Unit tests for retrieving a webpage."""

# pylint: disable=missing-function-docstring

import briefly.http

def test_get_html_body():
    text = briefly.http.get_html_text('https://www.cs.cmu.edu/~rgs/alice-I.html')
    assert text.startswith("Alice's Adventures in Wonderland -- Chapter I\nCHAPTER I\nDown the Rabbit-Hole\n")
