# Module 5: Word Embedding
# Word2Vec Load Model
# Author: Dr. Alfred

from gensim.models import Word2Vec
from nltk.corpus import gutenberg

embedding = Word2Vec.load('gutenberg_model')
print(embedding.most_similar('man', topn=5))