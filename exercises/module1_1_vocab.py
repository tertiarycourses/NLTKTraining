# Module 1: Get Started
# Extract Vocaubulary with Python
# Author: Dr. Alfred

text = """ Dostoevsky was the son of a doctor. 
His parents were very hard-working and deeply religious people,
but so poor that they lived with their five children in only
two rooms. The father and mother spent their evenings
in reading aloud to their children, generally from books of
a serious character."""

# text = open('sample.txt').read()

vocab = sorted(set(text.lower().split()))

print(vocab)
print("No of vocabulary : ",len(vocab))