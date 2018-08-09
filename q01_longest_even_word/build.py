# %load q01_longest_even_word/build.py
# Default imports

import re
from nltk.tokenize import word_tokenize

# Write your solution here :
def max_word(list_of_words):
    max_word_len = 0
    max_word = ''
    for word in list_of_words:
        if(len(word) > max_word_len):
            max_word_len = len(word)
            max_word = word
    return max_word
            
def q01_longest_even_word(sentence):
    list_of_even_word = [word for word in sentence.split() if len(word) % 2 == 0]
    if(len(list_of_even_word) > 0):
        return max_word(list_of_even_word)
    else :
        return 0


q01_longest_even_word('I am Ankit, from Mumbai')



