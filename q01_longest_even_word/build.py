# %load q01_longest_even_word/build.py
# Default imports

import re
# Write your solution here :
def q01_longest_even_word(sentence):
    list1 = [x for x in sentence.split(' ') if (len(x) % 2 == 0 and re.compile(r'\w').match(x)) ]
    if len(list1) == 0:
        return 0
    return max(list1, key=len)



