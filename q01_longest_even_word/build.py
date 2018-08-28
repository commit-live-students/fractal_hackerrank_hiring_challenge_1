# %load q01_longest_even_word/build.py
# Default imports

import re


# Write your solution here :
def q01_longest_even_word(sentence):
    ew = [x for x in sentence.split() if len(x)%2==0]
    print(ew)
    f1 = ''
    if len(ew) > 0:
        f1 = ew[0]
    for x in ew:
        if len(f1) < len(x):
            f1 = x
    if len(f1) > 0:
        return f1
    else: 
        return 0 








