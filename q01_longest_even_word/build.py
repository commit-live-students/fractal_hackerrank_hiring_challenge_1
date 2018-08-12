# %load q01_longest_even_word/build.py
# Default imports

import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Write your solution here :
#sentence = 'One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'

def q01_longest_even_word(sentence):
    words = word_tokenize(sentence)
    longest_even_word = 0
    for word in words:
        if len(word)%2 == 0 and len(word) > len(str(longest_even_word)):
            longest_even_word = word
            # print (longest_even_word)
    return longest_even_word

#q01_longest_even_word(sentence)



