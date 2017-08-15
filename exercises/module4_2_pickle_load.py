# Module 4: Text Classfication
# Load Model

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

# Step 4: Load the Pickle
import pickle
classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

# Step 5: Prediction/Evaluation
import nltk
print(classifier.classify(feature_extractor('Neo')))
print(nltk.classify.accuracy(classifier, test_set))