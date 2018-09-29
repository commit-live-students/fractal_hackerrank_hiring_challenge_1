# %load q01_longest_even_word/build.py
# Default imports

import re


# Write your solution here :
#def q01_longest_even_word(sentence):
    
    
x = 'My name is saurabh'

#def q01_longest_even_word(sentence)
mystr = 'My name is saurabh'

def q01_longest_even_word(sentence):
    even_list = [i for i in sentence.split() if len(i)%2==0]
    output = max(even_list, key=len) if even_list else 0
    return output



