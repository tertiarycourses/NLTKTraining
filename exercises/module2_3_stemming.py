# Module 2: Text Analysis with NLTK
# Stemming

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

#text = "respect, respects, respected, respecting, respectful, respectlfully"
text = "respect a respectful teacher"

words = word_tokenize(text)

print([ps.stem(w) for w in words])
