# Module 4: Text Classfication
# Save Model

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
import nltk
classifier = nltk.NaiveBayesClassifier.train(train_set)

# Step 6: Save the model
import pickle
save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()