# Module 3: Corpus
# Corpus structure challenge

from nltk.corpus import brown

# print(brown.fileids())

fileid = 'cl08'

# text = brown.words(fileid)
# print(text)

print(" Num of chars :",len(brown.raw(fileid)))
print(" Num of words :",len(brown.words(fileid)))
print(" Num of sentences :",len(brown.sents(fileid)))

print(" Categories:",brown.categories(fileid))

