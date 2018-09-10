# %load q01_longest_even_word/build.py
# Default imports
import re
from nltk.tokenize import sent_tokenize,word_tokenize


import nltk
nltk.download('punkt')
import re
from nltk.tokenize import sent_tokenize,word_tokenize


def q01_longest_even_word(data1):
#     sent_tokenize(data1)
#     tokens=[word_tokenize(i) for i in sent_tokenize(data1)]
#     u=[]#list consisting of all even words
#     for i in range(len(tokens)):
#         for j in range(len(tokens[i])):
#             if len(tokens[i][j])%2==0:
#                 u.append(tokens[i][j])
#     v=0 #variable initialised to zero for calculating max length of even nos
#     w=[]#list for storing final result of which we need the first element
#     for i in u:
#         if len(i)>v:
#             v=len(i)
#     for i in u:
#         if len(i)==v:
#             w.append(i)
#     if len(w)!=0:#check if list is empty or not
#         return w[0]
#     else:
#         return 0
    a=data1.replace('.','').replace(',','').split()
    b=[i for i in a if len(i)%2==0]
    maxlen=0
    for i in b:
        if len(i)>=maxlen:
            maxlen=len(i)
    maxl=[i for i in b if len(i)==maxlen]
    if len(maxl)==0:
        return(0)
    else:
        return(maxl[0])
            
    
    
    
    
    

    



data1='One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'

c=q01_longest_even_word(data1)
c
data1 = 'photographs or other images, readers can start to get a sense about the topic. This scanning and skimming helps set the expectation for the reading.'
c=q01_longest_even_word(data1)

c
data1 = ' testing very9 important'
c=q01_longest_even_word(data1)
c






