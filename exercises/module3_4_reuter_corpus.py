# Module 3: Corpus
# Reuters Corpus
# Author: Dr. Alfred

from nltk.corpus import reuters

# print(reuters.fileids())
# print(reuters.categories())

fileid = 'training/9865'

text = reuters.raw(fileid)
print(text)

print(" Num of chars :",len(reuters.raw(fileid)))
print(" Num of words :",len(reuters.words(fileid)))
print(" Num of sentences :",len(reuters.sents(fileid)))


print(reuters.categories(fileid))