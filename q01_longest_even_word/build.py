# %load q01_longest_even_word/build.py
# Default imports

import re
from nltk.tokenize import word_tokenize

data1 = 'One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'
data2 = 'photographs or other images, readers can start to get a sense about the topic. This scanning and skimming helps set the expectation for the reading.'
data3 = ' testing very9 important'

# Write your solution here :
def q01_longest_even_word(sentence = data1):
    words = re.split(r' ',sentence)
    even_words = []
    even_words_length = []
    
#loop to find even words and find its indices
    for x in words:
        if len(x)%2 == 0:
            even_words.append(x)
            even_words_length.append(len(x))
            max_length_index = even_words_length.index(max(even_words_length))
        else:
            even_word = 0

#Use the indices to return the word if present else return 0
    if even_words and even_words[max_length_index] != '':
        longest_even_word = even_words[max_length_index]
    else:
        longest_even_word = 0
    return longest_even_word




