# Module 3: Corpus
# Text statistics challenge

import nltk

text = "Today i learn Python in a Python class and think Python is awesome"
words = [w.lower() for w in text.split()]

distr = nltk.FreqDist(words)
print(distr.most_common(5))
print(distr["python"])