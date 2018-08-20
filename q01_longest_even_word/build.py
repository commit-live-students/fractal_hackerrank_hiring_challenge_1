# %load q01_longest_even_word/build.py
# Default imports

import nltk
nltk.download('punkt')

import re
from nltk.tokenize import word_tokenize
import numpy as np

# Write your solution here :
def q01_longest_even_word(text1):
    #Tokenize the words in a list and convert into array to perform map function
    tokens = word_tokenize(text1)
    #tokens = text1.split(' ')
    arr = np.array(tokens)
    token_count = np.array(list(map(lambda x: len(x), arr)))

    #initiate a even emply list and enumerate it to get list of even words
    even = []
    for i, v in enumerate(arr):
        if len(arr[i])%2 == 0:
            even.append(v)

    #convert it to numpy array to perform count of each and print max of even or first
    even = np.array(even)
    token_count = np.array(list(map(lambda x: len(x), even)))
    try:
        return (even[token_count.argmax()])
    except:
        return 0
    
text1 = ' testing very9 important'

q01_longest_even_word(text1)





