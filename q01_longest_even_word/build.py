# %load q01_longest_even_word/build.py
# Default imports

import re

# Write your solution here :
def q01_longest_even_word(sentence):
    tems = [ word for word in sentence.split() if len(word) % 2 == 0]
    if max(tems, key=len)== '' :
        return 0
    else:
        return max(tems, key=len)







