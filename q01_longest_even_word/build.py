# %load q01_longest_even_word/build.py
# Default imports

import re

# Write your solution here :
def q01_longest_even_word(sentence):
    #splitting string at space and create new list of splitted element
    elment_list = sentence.split()
    
    # list of element whose length is even
    even_list =  list(filter(lambda x: len(x)%2 == 0, elment_list))
    
    if even_list == []: # checking list is empty or not
        return 0
    
    length = 0 # for storing max value
    name = ''  # storing element which length is greatest in even_list
    for el in even_list:
        if length < len(el):
            length = len(el)
            name = el
            
    return name # returning name whose ha
sentence = 'One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'
q01_longest_even_word(sentence)

 


