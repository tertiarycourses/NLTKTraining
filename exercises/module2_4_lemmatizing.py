# Module 2: Text Analysis with NLTK
# Lemmatizing
# Author: Dr. Alfred

import nltk
from nltk.tokenize import word_tokenize

#text = "respect, respects, respected, respecting, respectful, respectfully"
# text = "respects a respectful teacher"
text = "Women buy things in the shopping mall"

words = word_tokenize(text.lower())

lemmatizer = nltk.WordNetLemmatizer()
print([lemmatizer.lemmatize(w) for w in words])
