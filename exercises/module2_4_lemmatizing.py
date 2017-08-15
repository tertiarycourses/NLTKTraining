# Module 2: Text Analysis with NLTK
# Lemmatizing

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

#text = "respect, respects, respected, respecting, respectful, respectfully"
text = "respect a respectful teacher"

words = word_tokenize(text)

lemmatizer = WordNetLemmatizer()
print([lemmatizer.lemmatize(w) for w in words])
