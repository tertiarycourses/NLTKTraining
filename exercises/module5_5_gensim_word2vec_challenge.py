# Module 5: Advanced Topics
# Gensime

from gensim.models import Word2Vec
from nltk.corpus import movie_reviews

embedding = Word2Vec(movie_reviews.sents(),min_count=1,size=10)

print(embedding.most_similar('man', topn=5))
print(embedding.most_similar('woman', topn=5))

# embedding.save('movie_model')
# embedding2 = Word2Vec.load('movie_model')
# print(embedding2.most_similar('man', topn=5))