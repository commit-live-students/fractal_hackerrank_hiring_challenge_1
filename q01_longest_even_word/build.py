# %load q01_longest_even_word/build.py
# Default imports

import re

#'My Name is Ramesh'
# Write your solution here :
def q01_longest_even_word(sentence):
  
    list1=[x for x in sentence.split() if len(x)%2==0]
    output=max(list1,key=len) if list1 else 0
    return output

q01_longest_even_word('My Name is Ram')








