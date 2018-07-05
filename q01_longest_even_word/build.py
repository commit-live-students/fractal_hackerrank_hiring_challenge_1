# Default imports

import re
from nltk.tokenize import word_tokenize

# Write your solution here :
def q01_longest_even_word(sentence):
    lst = [word for word in sentence.strip().split()]
    lstlen = [len(word) for word in sentence.strip().split()]
    evenmaxnum = 0
    try:
        for i in range(0,len(lstlen)):
            if (lstlen[i] % 2 == 0):
                if lstlen[i] > evenmaxnum:
                    evenmaxnum = lstlen[i]
                    evenmaxIndex = i
        return lst[evenmaxIndex]
    except:
        return 0
