# Module 2: Text Analysis with NLTK
# Stop Words

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))
#print(stop_words)

text = "Hello, Mr. Tan, how are you? Do you find NLTK fun and easy to use? I hope you do in this class"

words = word_tokenize(text)

filtered = [w for w in words if not w in stop_words]
print(filtered)
