# %load q01_longest_even_word/build.py
# Default imports

import re


# Write your solution here :
def q01_longest_even_word(sentence):
    w=sentence.split()
    v=[ y for y in w if len(y)%2==0 ]
    k=max(v,key=len) if v else 0
    return k
    




