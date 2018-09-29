# %load q01_longest_even_word/build.py
# Default imports

import re

sentence='Time t cod eve numbe'
# Write your solution here :
def q01_longest_even_word(sentence):
    s3=list(filter(lambda x:(len(x)%2==0), sentence.split()))
    output=max(s3,key=len) if s3 else 0
    return output




