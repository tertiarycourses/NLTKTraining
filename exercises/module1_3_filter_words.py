# Module 1: Get Started
# Filter words
# Author: Dr. Alfred

text = """ Dostoevsky was the son of a doctor. 
His parents were very hard-working and deeply religious people,
but so poor that they lived with their five children in only
two rooms. The father and mother spent their evenings
in reading aloud to their children, generally from books of
a serious character."""

vocab = sorted(set(text.lower().split()))
long_words = [word for word in vocab if len(word) > 5]
print(long_words)