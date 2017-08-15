# Module 5: Advanced Topics
# Grammar Parser

text = "I shot an elephant in my pajamas"


import nltk
from nltk import CFG
grammar = CFG.fromstring("""
	S -> NP VP
	PP -> P NP
	NP -> Det N | Det N PP | 'I'
	VP -> V NP | VP PP 
	Det -> 'an' | 'my'
	N -> 'elephant' | 'pajamas' 
	V -> 'shot' 
	P -> 'in'
	""")
parser = nltk.ChartParser(grammar)
for tree in parser.parse(text.split()):
	print(tree)

tree.draw()