from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

#print(brown_tagged_sents)
print(brown_sents)

