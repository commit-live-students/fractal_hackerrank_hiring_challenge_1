import sys
import nltk
from nltk.tokenize import word_tokenize

sentence = sys.argv[1]

def q01_longest_even_word(sentence):
    word=word_tokenize(sentence)
    list1 =[word for word in word if len(word) % 2 == 0]
    if(len(list1) == 0):
        return 0
    else:
        return max(list1, key = len)
