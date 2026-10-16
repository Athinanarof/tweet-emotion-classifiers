import re
from time import time

import nltk
from emoji import demojize

def preprocess(text, quiet=False):
  """Clean a pandas Series of tweets for tokenization.

    Lowercases, removes links and @mentions, converts emojis to words,
    expands negations ("can't" -> "can not"), keeps only letters,
    shrinks repeated letters ("soooo" -> "so"), and drops English
    stopwords except "not", "no" and "nor".

    Returns a Series of cleaned strings."""

  start = time()
  texts = texts.str.lower()

  