# %load q01_longest_even_word/build.py
# Default imports

import re
from nltk.tokenize import word_tokenize

data1 = 'One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'
data2 = 'photographs or other images, readers can start to get a sense about the topic. This scanning and skimming helps set the expectation for the reading.'
data3 = ' testing very9 important'

# Write your solution here :
def q01_longest_even_word(sentence):
    list1 = []
    list2 = []
    for i in sentence.split():
        list1.append(i)
    
    for j in list1:
        if (len(j)) % 2 == 0:
            list2.append(j)
    return(max(list2, key=len, default=0))
    

q01_longest_even_word(sentence = data2)


