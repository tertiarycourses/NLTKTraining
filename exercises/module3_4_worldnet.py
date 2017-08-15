# Module 3: Corpus
# WorldNet

from nltk.corpus import wordnet

# print(wordnet.synsets("motorcars"))
# print(wordnet.synsets("automobiles"))
print(wordnet.synsets("cars"))

# print(wordnet.synset('car.n.01').lemma_names())
# print(wordnet.synset('car.n.02').lemma_names())
# print(wordnet.synset('car.n.03').lemma_names())
# print(wordnet.synset('car.n.04').lemma_names())

# print(wordnet.synset('car.n.01').definition())

# synonyms = []

# for syn in wordnet.synsets("good"):
#     for l in syn.lemmas():
#         synonyms.append(l.name())

# print(set(synonyms))

# w1 = wordnet.synset('ship.n.01')
# w2 = wordnet.synset('boat.n.01')
# print(w1.wup_similarity(w2))