# Module 2: Text Analysis with NLTK
# Stop Words with NLTK
# Author: Dr. Alfred

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# print(stopwords.words('english')[0:500:25])

stop_words = set(stopwords.words("english"))

text = """ Dostoevsky was the son of a doctor. 
His parents were very hard-working and deeply religious people,
but so poor that they lived with their five children in only
two rooms. The father and mother spent their evenings
in reading aloud to their children, generally from books of
a serious character."""

print(word_tokenize(text))

# Remove stop words
filtered = [word for word in word_tokenize(text.lower()) if  word not in stop_words]
print("\n----- After Filtering the Stop Words -----\n")
print(filtered)
