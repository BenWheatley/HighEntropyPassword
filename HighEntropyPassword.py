#!/usr/bin/python

import random

f = open('/usr/share/dict/web2', 'r')
allWords = f.readlines()
f.close()

numOfWords = len(allWords)

wordIndex1 = random.randint(0, numOfWords)
wordIndex2 = random.randint(0, numOfWords)
wordIndex3 = random.randint(0, numOfWords)

separator1 = str(random.randint(0, 1000))
separator2 = str(random.randint(0, 1000))

print( allWords[wordIndex1].strip() + separator1 + allWords[wordIndex2].strip() + separator2 + allWords[wordIndex3].strip() )
