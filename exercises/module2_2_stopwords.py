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
stop_words = ['.',',','a','they','the','his','so','and','were','from','that','of','in','only','with','to']

print(word_tokenize(text))

# Remove stop words
text = word_tokenize(text.lower())

filtered = [word for word in text if word not in stop_words]
print("\n----- After Filtering the Stop Words -----\n")
print(filtered)
