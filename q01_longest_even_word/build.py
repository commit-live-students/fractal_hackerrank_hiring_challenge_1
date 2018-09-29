# %load q01_longest_even_word/build.py
# Default imports

import re

input1 = 'time to write a great code'

# Write your solution here :
def q01_longest_even_word(sentence):
    maxlen = 0
    input2 = sentence.split(' ')
    for i in input2: 
        if (len(i)%2 == 0 and len(i) > maxlen):
            maxlen = len(i)
            finalop = i
    
    if maxlen == 0: 
        return (0)
    else:
        return (finalop)
data1 = 'One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'
data2 = 'photographs or other images, readers can start to get a sense about the topic. This scanning and skimming helps set the expectation for the reading.'
data3 = ' testing very9 important'
q01_longest_even_word(data3)


