# %load q01_longest_even_word/build.py
# Default imports

import re

# Write your solution here :
def q01_longest_even_word(sentence):
    
    words = sentence.split(' ')
    evenWords = [word for word in words if (len(word) != 0) & (len(word)%2 == 0)]
    
    if(len(list(evenWords)) > 0):
        maxLenWord = max(evenWords, key=len)
        return maxLenWord
    else:
        return 0
    
data1 = 'One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'
data2 = 'photographs or other images, readers can start to get a sense about the topic. This scanning and skimming helps set the expectation for the reading.'
data3 = ' testing very9 important'
q01_longest_even_word(data3)





