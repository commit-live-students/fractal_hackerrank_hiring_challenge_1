# %load q01_longest_even_word/build.py
# Default imports

import re


# Write your solution here :
def q01_longest_even_word(sentence='My name1 is1 Akshay1'):
    y=[]
    x=sentence.split()
    for i in x:
        if len(i)%2==0:
            y.append(i)
    longest_word=max(y,key=lambda word:len(word)) if y else 0
    return longest_word
    
    

q01_longest_even_word('photographs or other images, readers can start to get a sense about the topic. This scanning and skimming helps set the expectation for the reading.')


