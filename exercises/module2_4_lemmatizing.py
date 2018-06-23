# Module 2: Text Analysis with NLTK
# Lemmatizing
# Author: Dr. Alfred

import nltk
from nltk.tokenize import word_tokenize

text = "running run"

text ="meanness meaning"

# text = "Women buy things in the shopping mall"

words = word_tokenize(text.lower())

lemmatizer = nltk.WordNetLemmatizer()
print([lemmatizer.lemmatize(w) for w in words])
