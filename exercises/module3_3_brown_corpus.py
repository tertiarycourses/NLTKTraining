# Module 3: Corpus
# Brown Corpus
# Author: Dr. Alfred

from nltk.corpus import brown
#print(brown.categories())

text = brown.raw(categories='news')
print(text)

print(" Num of chars :",len(brown.raw(categories='news')))
print(" Num of words :",len(brown.words(categories='news')))
print(" Num of sentences :",len(brown.sents(categories='news')))