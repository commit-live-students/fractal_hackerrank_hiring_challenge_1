# %load q01_longest_even_word/build.py
# Default imports

import re
from nltk.tokenize import word_tokenize

# Write your solution here :
def q01_longest_even_word(words):
    words = words.split(' ')
    max_length = 0;''
    result = ''
    for x in words:
        if len(x) % 2 == 0 and len(x) > max_length:
            max_length = len(x)
            result = x
    if max_length <= 0:
        return 0
    else:
        return result


