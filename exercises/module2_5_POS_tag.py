# Module 2: Text Analysis with NLTK
# POS Tagging

# Noun
# import nltk
# print(nltk.pos_tag(['cat']))

# Verb
# import nltk
# print(nltk.pos_tag(['run']))

# Adjective
# import nltk
# print(nltk.pos_tag(['delicious','food']))

# Adword
# import nltk
# print(nltk.pos_tag(['run','slowly']))

from nltk.tokenize import word_tokenize
text = "Hello, Mr. Tan, how are you? Do you find NLTK fun and easy to use? I hope you do in this class"
words = word_tokenize(text)


# import nltk
# tagged = nltk.pos_tag(words)
# print(tagged)


