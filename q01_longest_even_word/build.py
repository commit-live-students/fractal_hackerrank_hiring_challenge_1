# %load q01_longest_even_word/build.py
# Default imports
import sys
import re
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
#data1 = 'One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'
#sentence = 'photographs or other images, readers can start to get a sense about the topic. This scanning and skimming helps set the expectation for the reading.'
data3 = ' testing very9 important'

# Write your solution here :
def q01_longest_even_word(data3):
    word=word_tokenize(data3)
    list1 =[word for word in word if len(word) % 2 == 0]
    if(len(list1) == 0):
        return 0
    else:
        return max(list1, key = len)
    
q01_longest_even_word(data3)


