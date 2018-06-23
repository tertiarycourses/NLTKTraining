# Module 2: Text Analysis with NLTK
# Token Challenge
# Author: Dr. Alfred

from urllib import request

url="https://en.wikipedia.org/wiki/George_Washington"
response = request.urlopen(url)
text = response.read().decode('utf8')

from nltk.tokenize import sent_tokenize, word_tokenize

# tokens = word_tokenize(text)
tokens = sent_tokenize(text)

print(len(tokens))
