# Module 4: Text Classificaton
# Bi-gram
# Author: Dr. Alfred

import nltk
from nltk import bigrams
from nltk.tokenize import word_tokenize

text = """ Dostoevsky was the son of a doctor. 
His parents were very hard-working and deeply religious people,
but so poor that they lived with their five children in only
two rooms. The father and mother spent their evenings
in reading aloud to their children, generally from books of
a serious character."""

ngrams = bigrams(word_tokenize(text))
print(list(ngrams))