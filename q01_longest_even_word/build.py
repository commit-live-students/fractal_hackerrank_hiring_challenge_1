# %load q01_longest_even_word/build.py
# Default imports

import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
# Write your solution here :
def q01_longest_even_word(sentence):
    words = word_tokenize(sentence)
    longest_word = 0
    for word in words:
        if len(word)%2==0 and len(word)>len(str(longest_word)):
            longest_word=word
    return longest_word

