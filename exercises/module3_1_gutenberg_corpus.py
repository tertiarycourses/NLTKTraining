# Module 3: Corpus
# Gutenberg Corpus
# Author: Dr. Alfred

from nltk.corpus import gutenberg

# print(gutenberg.fileids())

fileid = 'austen-emma.txt'
text = gutenberg.raw(fileid)
print(text)

print(" Num of chars :",len(gutenberg.raw(fileid)))
print(" Num of words :",len(gutenberg.words(fileid)))
print(" Num of sentences :",len(gutenberg.sents(fileid)))


