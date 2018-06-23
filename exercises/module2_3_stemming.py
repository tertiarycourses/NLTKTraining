# Module 2: Text Analysis with NLTK
# Stemming
# Author: Dr. Alfred

from nltk.stem import PorterStemmer,LancasterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()
# stemmer = LancasterStemmer()


# Sucess Cases
text = "running run"

# Failed Cases
#text ="meanness, meaning"


words = word_tokenize(text)

print([stemmer.stem(w) for w in words])
