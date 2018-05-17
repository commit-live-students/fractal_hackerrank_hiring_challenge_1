# Default imports

import re
from nltk.tokenize import word_tokenize

# Write your solution here :
def q01_longest_even_word(sentence):
    li = sentence.split()
    lar_str = ''
    l = 0
    for val in li:
        if len(val) % 2 == 0:
            if lar_str == '' and l == 0:
                lar_str = val
                l = len(val)

            else:
                if len(val) > l:
                    lar_str = val
                    l = len(val)

    if lar_str == '':
        lar_str = 0

    return lar_str
