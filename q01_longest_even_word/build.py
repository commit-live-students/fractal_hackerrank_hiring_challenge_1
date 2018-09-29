# %load q01_longest_even_word/build.py
# Default imports

import re


def q01_longest_even_word(sentence):
    x=[]
    sentence=sentence.split()
    for word in sentence:
        if len(word)%2==0: 
            x.append(word)
    
    longest_word=max(x,key=lambda word:len(word)) if x else 0 
    return longest_word
          
    

q01_longest_even_word('photographs or other images, readers can start to get a sense about the topic. This scanning and skimming helps set the expectation for the reading.')


