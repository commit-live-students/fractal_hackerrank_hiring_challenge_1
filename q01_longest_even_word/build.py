# %load q01_longest_even_word/build.py
# Default imports

import re


# Write your solution here :
def q01_longest_even_word(sentence):
    words = list(filter(lambda x: len(x)%2 == 0, sentence.split()))
    if len(words) > 0: 
        max_len = len(max(words, key=len))
        return [word for word in words if len(word) == max_len][0]
    else:
        return 0
    

sentence = 'One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'
type(sentence.split())

words = sentence.split()
max_len = len(max(sentence.split(), key=len))
if max_len%2 == 0:
    [word for word in words if len(word) == max_len][0]
else:
    0
q01_longest_even_word(sentence)



