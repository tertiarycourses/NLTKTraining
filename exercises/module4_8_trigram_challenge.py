# Module 4: Text Classificaton
# Tri-gram
# Author: Dr. Alfred

import nltk
from nltk import bigrams,trigrams
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

stop_words = set(stopwords.words("english"))

text = """ Dostoevsky was the son of a doctor. 
His parents were very hard-working and deeply religious people,
but so poor that they lived with their five children in only
two rooms. The father and mother spent their evenings
in reading aloud to their children, generally from books of
a serious character."""

def is_ok(token):
    return re.match('^[a-z]+$', token) and token not in stop_words

filtered = [word for word in word_tokenize(text.lower()) if is_ok(word)]


ngrams = trigrams(filtered)
print(list(ngrams))