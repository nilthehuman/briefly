"""A tool to roughly identify the topic of English text input."""

import sys

from .briefly import *

MIN_PYTHON = (3, 6)
if sys.version_info < MIN_PYTHON:
    sys.exit("Please use Python %s.%s or later.\n" % MIN_PYTHON)
