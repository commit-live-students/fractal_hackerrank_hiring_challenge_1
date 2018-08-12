# %load q01_longest_even_word/build.py
# Default imports
import sys
import numpy as np
import nltk
nltk.download('punkt')
import re
from nltk.tokenize import word_tokenize
#nltk.download('punkt')
sentence='One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'
# Write your solution here :
def q01_longest_even_word(sentence):
        words=word_tokenize(sentence)
        longest_word=0
    #list1=[word for word in sentence.split()
        for word in words:
             if len(word)%2==0 and len(word)>len(str(longest_word)):
                    longest_word=word
        return longest_word
  
    
#q01_longest_even_word('helo worlddd')
q01_longest_even_word(sentence)
    





