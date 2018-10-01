# %load q01_longest_even_word/build.py
# Default imports

import re


# Write your solution here :
def q01_longest_even_word(sentence):
    l1=sentence.split()
    
    for x in l1[:]:
        if (len(x)%2!=0):
            l1.remove(x)
                        
            
    return max(l1,key=len,default=0)
     
            

             
 
        
    
    

    

q01_longest_even_word('My name is Simran')



