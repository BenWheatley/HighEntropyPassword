#!/usr/bin/python

import random
import string

f = open('/usr/share/dict/web2', 'r')
allWords = f.readlines()
f.close()

numOfWords = len(allWords)

wordIndex1 = random.randint(0, numOfWords-1)
wordIndex2 = random.randint(0, numOfWords-1)
wordIndex3 = random.randint(0, numOfWords-1)

separator1 = str(random.randint(0, 1000))
separator2 = str(random.randint(0, 1000))

print("\nCorrect Horse Battery Staple:")
print( allWords[wordIndex1].strip() + separator1 + allWords[wordIndex2].strip() + separator2 + allWords[wordIndex3].strip() )


#-----------------

chars = list(string.ascii_letters + string.digits + string.punctuation)
numChars = len(chars)
randomString = ""
for x in range(0, 12):
	charIndex = random.randint(0, numChars-1)
	randomString = randomString + chars[charIndex]
print("\n12 random characters from set [a-Z, digits, punctuation]:")
print(randomString)
print
