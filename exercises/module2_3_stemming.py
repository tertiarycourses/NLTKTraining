# Module 2: Text Analysis with NLTK
# Stemming
# Author: Dr. Alfred

from nltk.stem import PorterStemmer,LancasterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()
# stemmer = LancasterStemmer()

text = "respect, respects, respected, respecting, respectful, respectlfully"
#text = "using use used uses"
#text = "respect a respectful teacher"

words = word_tokenize(text)

print([stemmer.stem(w) for w in words])
