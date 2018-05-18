# %load q01_longest_even_word/build.py
# Default imports

import re
from nltk.tokenize import word_tokenize

# Write your solution here :
def q01_longest_even_word(d):
    d=d.replace(',','')
    d=d.replace('.','')
    d=d.split()
    
    max_len=0
    maxx=0
    for word in d:
        if len(word)%2==0 and maxx<len(word):
         
            max_len=word
            maxx=len(word)
        
    return max_len

