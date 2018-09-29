# %load q01_longest_even_word/build.py
# Default imports

import re


# Write your solution here :
def q01_longest_even_word(sentence):
    a= sentence.split()
    b= list(filter(lambda x:x if len(x)%2 == 0 else 0,a))
    
    if len(b)>0:
        return max(b,key=len)
    else:
        return 0
    
    return b

    
    

sentence= ''
q01_longest_even_word(sentence)


