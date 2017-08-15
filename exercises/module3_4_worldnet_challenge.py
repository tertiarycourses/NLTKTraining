# Module 3: Corpus
# WorldNet challenge

from nltk.corpus import wordnet

# print(wordnet.synsets("rat"))
# print(wordnet.synsets("mouse"))


w1 = wordnet.synset('rat.n.01')
w2 = wordnet.synset('mouse.n.01')
print(w1.wup_similarity(w2))