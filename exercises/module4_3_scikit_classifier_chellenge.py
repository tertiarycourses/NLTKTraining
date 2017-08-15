# Module 4: Text Classfication
# Scikit Classifer Model Challenge

# Step 1: Load Data
from nltk.corpus import names
labeled_names = ([(name, 'male') for name in names.words('male.txt')]
	+ [(name, 'female') for name in names.words('female.txt')])

import random
random.shuffle(labeled_names)

# Step 2: Extract last letter of a name as the feature
def feature_extractor(name):
	return {'last_letter': name[-1]}

featureset = [(feature_extractor(name), gender) for (name, gender) in labeled_names]

# Step 3: Split the feature set to training/testing datasets

train_set, test_set = featureset[500:], featureset[:500]

# Step 4/5: Load the classifier and perform training
from nltk.classify.scikitlearn import SklearnClassifier
# from sklearn.naive_bayes import MultinomialNB
# classifier = SklearnClassifier(MultinomialNB())
# from sklearn.linear_model import LogisticRegression
# classifier = SklearnClassifier(LogisticRegression())
from sklearn.svm import SVC
classifier = SklearnClassifier(SVC())
classifier.train(train_set)


# Step 6: Prediction/Evaluation
print(classifier.classify(feature_extractor('Neo')))
import nltk
print(nltk.classify.accuracy(classifier, test_set))
