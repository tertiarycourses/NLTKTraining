# Module 2: Text Analysis with NLTK
# Chucking
# Author: Dr. Alfred

import nltk
from nltk.tokenize import word_tokenize
from nltk import chunk

text = "The white dog fight with a black cat"
words = word_tokenize(text)
tagged = nltk.pos_tag(words)

grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(tagged)
print(result)
result.draw()

