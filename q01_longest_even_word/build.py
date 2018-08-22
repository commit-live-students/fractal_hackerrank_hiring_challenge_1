# %load q01_longest_even_word/build.py
# Default imports

import re
from nltk.tokenize import word_tokenize

# Write your solution here :
def q01_longest_even_word(sentence):
#     tokens = word_tokenize(sentence)
    tokens = (sentence.strip()).split(' ')
    lenghts_of_tokens = [len(token) for token in tokens if len(token) % 2 == 0]
    if len(lenghts_of_tokens) > 0:
        max_length = max(lenghts_of_tokens)
        for token in tokens:
            if len(token) == max_length:
                return token
    return 0
q01_longest_even_word('dhdhdhdhdhdhdhdhd dhdhdhdhd')


