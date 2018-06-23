# Module 2: Text Analysis with NLTK
# Regular Expresion
# Author: Dr. Alfred

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

text = """ Dostoevsky was the son of a doctor. 
His parents were very hard-working and deeply religious people,
but so poor that they lived with their five children in only
two rooms. The father and mother spent their evenings
in reading aloud to their children, generally from books of
a serious character."""

#text2 = [word for word in word_tokenize(text.lower()) if re.search('^d', word)]
#text2 = [word for word in word_tokenize(text.lower()) if re.search('s$', word)]
text2 = [word for word in word_tokenize(text.lower()) if re.match('^[a-z]+$', word)]

print(text2)
