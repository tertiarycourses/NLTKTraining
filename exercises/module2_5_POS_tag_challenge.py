# Module 2: Text Analysis with NLTK
# POS Tagging Challenge
# Author: Dr. Alfred

import nltk
# print(nltk.pos_tag(['cat','cats']))
# print(nltk.pos_tag(['take','took','taking','taken']))
# print(nltk.pos_tag(['delicious']))
# print(nltk.pos_tag(['slowly']))

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

stop_words = set(stopwords.words("english"))

text = """ Dostoevsky was the son of a doctor. 
His parents were very hard-working and deeply religious people,
but so poor that they lived with their five children in only
two rooms. The father and mother spent their evenings
in reading aloud to their children, generally from books of
a serious character."""

words = word_tokenize(text)

def is_ok(token):
    return re.match('^[a-z]+$', token) and token not in stop_words

filtered = [word for word in word_tokenize(text.lower()) if is_ok(word)]

import nltk
tagged = nltk.pos_tag(filtered)
print(tagged)


