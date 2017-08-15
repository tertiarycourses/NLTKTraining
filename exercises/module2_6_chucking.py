# Module 2: Text Analysis with NLTK
# Chucking

from nltk.tokenize import word_tokenize

text = "Hello, Mr. Tan, how are you? Do you find NLTK fun and easy to use? I hope you do in this class"
words = word_tokenize(text)

import nltk
tagged = nltk.pos_tag(words)

from nltk import chunk
tree = chunk.ne_chunk(tagged)
print(tree)
# tree.draw()
