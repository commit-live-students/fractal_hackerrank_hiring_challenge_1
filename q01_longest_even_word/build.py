# %load q01_longest_even_word/build.py
# Default imports

import re

b = 0

# Write your solution here :
def q01_longest_even_word(sentence):
      # split the string  
    s = sentence.split()
    ev_li = []
    for i in s: 
        if (len(i) % 2 == 0):
            ev_li.append(i) 
    if ev_li == []:
        b=0
    if ev_li != []:
        b = max(ev_li, key=len)
    
    return b
    


