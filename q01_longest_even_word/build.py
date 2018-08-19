# %load q01_longest_even_word/build.py
# Default imports

import re
from nltk.tokenize import word_tokenize

data1 = 'One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'
data2 = 'photographs or other images, readers can start to get a sense about the topic. This scanning and skimming helps set the expectation for the reading.'
data3 = ' testing very9 important'

# Write your solution here :
def q01_longest_even_word(sentence):
    even_list = [x for x in sentence.split() if len(x) % 2 == 0]
    
    if len(even_list) > 0:
        word = max(even_list, key=len)
    else:
        word = 0
   
    return word
    
print(q01_longest_even_word(data1))



