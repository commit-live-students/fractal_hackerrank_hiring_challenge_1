# %load q01_longest_even_word/build.py
# Default imports

import re


# Write your solution here :
def q01_longest_even_word(sentence):
    list11 = [word for word in sentence.split() if len(word) % 2 == 0 ]
    if len(list11) == 0:
        longest = 0
    else:
        longest = max(list11, key = len)
    return longest

    
    


