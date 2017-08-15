# Module 3: Corpus
# Text statistics

from nltk.corpus import brown

import nltk
cfd = nltk.ConditionalFreqDist(
	(genre, word) 
	for genre in brown.categories() 
	for word in brown.words(categories=genre))

genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']

cfd.tabulate(conditions=genres, samples=modals)

# import nltk
# from nltk.corpus import movie_reviews

# print(movie_reviews.fileids())
# print(movie_reviews.categories("pos/cv997_5046.txt"))
# print(movie_reviews.words("pos/cv997_5046.txt"))


# words = [w.lower() for w in movie_reviews.words()]

# distr = nltk.FreqDist(words)
# print(distr.most_common(15))
# print(distr["stupid"])