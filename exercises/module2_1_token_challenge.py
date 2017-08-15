# Module 2: Text Analysis with NLTK
# Token Challenge

from urllib import request
url = "http://www.gutenberg.org/files/2554/2554.txt"
response = request.urlopen(url)
text = response.read().decode('utf8')

from nltk.tokenize import sent_tokenize, word_tokenize

#tokens = word_tokenize(text)
tokens = sent_tokenize(text)

print(len(tokens))
