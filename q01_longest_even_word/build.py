# %load q01_longest_even_word/build.py
# Default imports

import re
from nltk.tokenize import word_tokenize

# Write your solution here :
def q01_longest_even_word(sentence):
    output = '0'
    ch = sentence.split(' ')
    for i in ch :
        if (len(i) % 2 ==0  ) :
            if len(output) < len(i) :
                output = i
    if (output == '0'):
        output =0
        
    return output
               


