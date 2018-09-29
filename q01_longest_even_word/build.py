# %load q01_longest_even_word/build.py
# Default imports

import re

a='my name is Bhavesh'
# Write your solution here :
mystr='my name is Bhavesh'
def q01_longest_even_word(sentence):
    even_list = [x for x in sentence.split() if len(x)%2==0]
    output = max(even_list, key=len) if even_list else 0
    return output
    


