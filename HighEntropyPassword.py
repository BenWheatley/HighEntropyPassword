#!/usr/bin/python

import random
import string
import math

f = open('/usr/share/dict/web2', 'r')
allWords = f.readlines()
f.close()

numOfWords = len(allWords)

secureRNG = random.SystemRandom()

wordIndex1 = secureRNG.randint(0, numOfWords-1)
wordIndex2 = secureRNG.randint(0, numOfWords-1)
wordIndex3 = secureRNG.randint(0, numOfWords-1)

separator1 = str(secureRNG.randint(0, 1000))
separator2 = str(secureRNG.randint(0, 1000))

print("\nCorrect Horse Battery Staple (73 bits entropy, if random number generator is correct and your dictionary is the same size as mine):")
print( allWords[wordIndex1].strip() + separator1 + allWords[wordIndex2].strip() + separator2 + allWords[wordIndex3].strip() )


#-----------------

chars = list(string.ascii_letters + string.digits + string.punctuation)
numChars = len(chars)
randomString = ""
length = 12
for x in range(0, length):
	charIndex = secureRNG.randint(0, numChars-1)
	randomString = randomString + chars[charIndex]

entropy = math.log(chars.__len__() ** length, 2) # Can't use math.log2(...) because that's python 3
print("\n12 random characters from set [a-Z, digits, punctuation] ("+str(entropy)+" bits of entropy, if random number generator is correct):")
print(randomString)
print
