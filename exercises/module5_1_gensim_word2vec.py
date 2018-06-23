# Module 5: Word Embedding
# Gutenberg Word2Vec
# Author: Dr. Alfred

from gensim.models import Word2Vec
from nltk.corpus import gutenberg

embedding = Word2Vec(gutenberg.sents(),min_count=1, window=5, size=32)

print(embedding['man'])
print(embedding.most_similar('man', topn=5))
print(embedding.most_similar('woman', topn=5))

print(embedding.most_similar(positive=['woman', 'king'], negative=['man']))