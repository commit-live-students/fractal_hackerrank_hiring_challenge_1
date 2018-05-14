# %load q01_longest_even_word/build.py
# Default imports

import re
from nltk.tokenize import word_tokenize

data1 = 'One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'
data2 = 'photographs or other images, readers can start to get a sense about the topic. This scanning and skimming helps set the expectation for the reading.'
data3 = ' testing very9 important'

# Write your solution here :
def q01_longest_even_word(sentence):
    maxLen = 0
    maxLenWord = ''
    l = sentence.split(' ')
    a = [x for x in l if len(x.strip())%2 == 0 and len(x.strip())>0]
    for w in a:
        if(len(w)>maxLen):
            maxLen = len(w)
            maxLenWord = w
    if(len(a)>0):
        return maxLenWord
    else:
        return 0



