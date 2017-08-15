from nltk.corpus import gutenberg

# print(gutenberg.fileids())

#fileid = 'austen-emma.txt'
fileid = 'austen-sense.txt'

text = gutenberg.words(fileid)
#print(text)

# print(" Num of chars :",len(gutenberg.raw(fileid)))
# print(" Num of words :",len(gutenberg.words(fileid)))
# print(" Num of sentences :",len(gutenberg.sents(fileid)))

print(gutenberg.category(fileid))

