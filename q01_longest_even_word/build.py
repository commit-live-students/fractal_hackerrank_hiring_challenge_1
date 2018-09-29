# %load q01_longest_even_word/build.py
# Default imports

import re


# Write your solution here :
def q01_longest_even_word(sentence):
    #sentence='My1 named ist Prteeti'
    even_list = [x for x in sentence.split() if len(x) % 2 == 0]
    output = max(even_list, key=len) if even_list else 0
    return output

q01_longest_even_word('My1 namd isd Prseeti')


