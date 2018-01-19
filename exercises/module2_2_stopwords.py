# Module 2: Text Analysis with NLTK
# Stop Words
# Author: Dr. Alfred

from nltk.tokenize import word_tokenize

text = """ Dostoevsky was the son of a doctor. 
His parents were very hard-working and deeply religious people,
but so poor that they lived with their five children in only
two rooms. The father and mother spent their evenings
in reading aloud to their children, generally from books of
a serious character."""

# Create a set of stop words
stop_words = set('. , very was were their from so but that for a of the and to in'.split())

print(word_tokenize(text))

# Remove stop words
filtered = [word for word in word_tokenize(text.lower()) if  word not in stop_words]
print("\n----- After Filtering the Stop Words -----\n")
print(filtered)
