# Module 4: Text Classfication
# Challenge

import nltk

# Step 1: Load Data 
from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

import random
random.shuffle(documents)

# Step 2: Extract Feature
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())
all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:3000]

def feature_extractor(review):
    words = set(review)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features
    
featureset = [(feature_extractor(review), sentiment) for (review, sentiment) in documents]


# Step 3: Split the feature set to training/testing datasets
training_set, testing_set = featureset[:1900],featureset[1900:]

# Step 4/5: Load the classifier and perform training
classifier = nltk.NaiveBayesClassifier.train(training_set)

# Step 6: Prediction/Evaluation
print("Classifier accuracy:",nltk.classify.accuracy(classifier, testing_set))
classifier.show_most_informative_features(15)
