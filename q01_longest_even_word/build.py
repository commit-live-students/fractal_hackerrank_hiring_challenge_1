# %load q01_longest_even_word/build.py
# Default imports

import re
from nltk.tokenize import word_tokenize

# Write your solution here :
sentence = 'photographs or other images, readers can start to get a sense about the topic. This scanning and skimming helps set the expectation for the reading.'
data1 = 'One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'

def q01_longest_even_word(sentence):
    new = sentence.split(' ')
    for x in new:
        if x == '':
            new.pop(0)
    even = [x for x in new if len(x)%2 == 0]
    if len(even) != 0:
        return max(even,key = len)
    if len(even) == 0:
        return 0
q01_longest_even_word(data1)
# a = ' testing very9 important'
# new = a.split(' ')
# even = [x for x in new if len(x)%2 == 0]
# for x in new:
#     if x == '':
#         new.pop(0)
# new


