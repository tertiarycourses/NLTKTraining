# Module 2: Text Analysis with NLTK
# Read Document
# Author: Dr. Alfred

from nltk.tokenize import sent_tokenize, word_tokenize

f = open('./corpus/document.txt')
text = f.read()

print(sent_tokenize(text))
#print(word_tokenize(text))

