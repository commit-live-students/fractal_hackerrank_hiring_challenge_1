# %load q01_longest_even_word/build.py
# Default imports

import re


# Write your solution here :
def q01_longest_even_word(sentence):
    splitted_text_list = sentence.split()
    list_with_even_length_words = list(filter(lambda x:len(x)%2==0, splitted_text_list))
    if len(list_with_even_length_words) > 0:
        return max(list_with_even_length_words, key=len)
    else:
        return 0
    

q01_longest_even_word('')


