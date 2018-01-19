# Module 5: Word Embedding
# Word2Vec Save Model
# Author: Dr. Alfred

from gensim.models import Word2Vec
from nltk.corpus import gutenberg

embedding = Word2Vec(gutenberg.sents(),min_count=1,size=32,sg=1)

print(embedding.most_similar('man', topn=5))
print(embedding.most_similar('woman', topn=5))

embedding.save('gutenberg_model')

