# Module 2: Text Analysis with NLTK
# Tokenizing Text 
# Author: Dr. Alfred

from nltk.tokenize import word_tokenize,sent_tokenize

text = """ Dostoevsky was the son of a doctor. 
His parents were very hard-working and deeply religious people,
but so poor that they lived with their five children in only
two rooms. The father and mother spent their evenings
in reading aloud to their children, generally from books of
a serious character."""

print(sent_tokenize(text))
print(word_tokenize(text))



