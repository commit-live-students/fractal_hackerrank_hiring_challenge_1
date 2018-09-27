# %load q01_longest_even_word/build.py
# Default imports

import re


# Write your solution here :
def q01_longest_even_word(sentence):
    words = sentence.split()
    even = ''
    
    for word in words:
        if len(word)%2==0 and len(word)>len(even):
            even = word
            
    if len(even)>0:
        return even
    else:
        return 0

q01_longest_even_word(' testing very9 important')

