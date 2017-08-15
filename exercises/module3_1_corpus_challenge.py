# Module 3: Corpus
# Challenge

from nltk.corpus import gutenberg
text = gutenberg.raw("austen-sense.txt")

from nltk.tokenize import sent_tokenize
token = sent_tokenize(text)
print(token[:5])