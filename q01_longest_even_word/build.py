# %load q01_longest_even_word/build.py
# Default imports

import re


# Write your solution here :
def q01_longest_even_word(sentence):
    
    max = 0
    data = sentence.split()
    long_word = 0
    for i in data:
        if(len(i) % 2 == 0):
            if(len(i) > max):
                max = len(i)
                long_word = i
    return long_word

q01_longest_even_word(' testing very9 important')



