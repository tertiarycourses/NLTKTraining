# Module 2: Text Analysis with NLTK
# POS Tagging
# Author: Dr. Alfred

import nltk
# print(nltk.pos_tag(['cat','cats']))
# print(nltk.pos_tag(['take','took','taking','taken']))
# print(nltk.pos_tag(['delicious']))
# print(nltk.pos_tag(['slowly']))

from nltk.tokenize import word_tokenize

text = """ Dostoevsky was the son of a doctor. 
His parents were very hard-working and deeply religious people,
but so poor that they lived with their five children in only
two rooms. The father and mother spent their evenings
in reading aloud to their children, generally from books of
a serious character."""

words = word_tokenize(text)

import nltk
tagged = nltk.pos_tag(words)
print(tagged)


