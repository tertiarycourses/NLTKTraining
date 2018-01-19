# Module 3: Corpus
# Frequency Distribution
# Author: Dr. Alfred


import nltk
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
import re

stop_words = set(stopwords.words("english"))

fileid = 'pos/cv971_10874.txt'
text = movie_reviews.words(fileid)

# Remove punctuations
def is_ok(token):
    return re.match('^[a-z]+$', token) and token not in stop_words

words = [word.lower() for word in text if is_ok(word)]

distr = nltk.FreqDist(words)
print(distr.most_common(5))
print(distr["stone"])

