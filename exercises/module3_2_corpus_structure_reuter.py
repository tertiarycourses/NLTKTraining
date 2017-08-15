# Module 3: Corpus
# Corpus structure challenge - reuters

from nltk.corpus import reuters

print(reuters.fileids())

fileid = 'training/9995'

# text = reuters.words(fileid)
# print(text)

print(" Num of chars :",len(reuters.raw(fileid)))
print(" Num of words :",len(reuters.words(fileid)))
print(" Num of sentences :",len(reuters.sents(fileid)))

print(" Categories:",reuters.categories(fileid))

