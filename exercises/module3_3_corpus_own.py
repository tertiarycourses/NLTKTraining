# Module 3: Corpus
# Create your own corpus

from nltk.corpus import PlaintextCorpusReader
corpus_root = 'corpus' 
my_corpus = PlaintextCorpusReader(corpus_root, '.*')

# print(my_corpus.fileids())

fileid = 'file1.txt'

text = my_corpus.words(fileid)
print(text)

print(" Num of chars :",len(my_corpus.raw(fileid)))
print(" Num of words :",len(my_corpus.words(fileid)))
print(" Num of sentences :",len(my_corpus.sents(fileid)))



