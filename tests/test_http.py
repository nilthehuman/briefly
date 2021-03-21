"""Unit tests for retrieving a webpage."""

# pylint: disable=missing-function-docstring

import briefly.http

def test_get_html_body():
    body = briefly.http.get_html_body('https://www.cs.cmu.edu/~rgs/alice-I.html')
    assert body.startswith("\nCHAPTER I\nDown the Rabbit-Hole\n\n")
