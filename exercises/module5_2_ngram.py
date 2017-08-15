# Module 5: Advanced Topics
# N-gram

import nltk
from nltk import bigrams
string = "I really like python, it's pretty awesome."
string_bigrams = bigrams(string)
print(list(string_bigrams))