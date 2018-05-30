# %load q01_longest_even_word/build.py
# Default imports

import re
from nltk.tokenize import word_tokenize

# Write your solution here :
def q01_longest_even_word(sentence):
    data_list = sentence.replace('.','').replace(',',' ').split(' ')  
    le = max(len(str1) for str1 in data_list if len(str1) % 2 == 0)
    if le != 0:
        word = next(str1 for str1 in data_list if len(str1) == le)
    return le if le == 0 else word


