# %load q01_longest_even_word/build.py
# Default imports

#import re
# Write your solution here :

import re

# Write your solution here :
def q01_longest_even_word(sentence):
    x=sentence.split()
    cond = [ word for word in x if len(word) % 2 == 0]
    print (cond)
    if not cond:
        return 0
    else:
        return max(cond, key=len)

re

q01_longest_even_word('a bbb cccccc ddd')







