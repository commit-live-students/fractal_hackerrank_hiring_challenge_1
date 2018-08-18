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
#     g=[]
#     for i in tokens[0]:
#         if len(i)%2==0:
#             g.append(i)
#     word1=max(g,key=lambda s: (len(s),s))#unusual line of code
#     j=0
#     maxlen1=[]
#     for i in g:
#         if len(i)>j:
#             j=len(i)
#     for i in g:
#         if len(i)==j:
#             maxlen1.append(i)
    
#     sent_tokenize(data1)
#     token1=[word_tokenize(i) for i in sent_tokenize(data1)]
#     u=[]
#     for i in token1[0]:
#         if len(i)%2==0:
#             u.append(i)
#     for i in token1[1]:
#         if len(i)%2==0:
#             u.append(i)
#     v=0
#     for i in u:
#         if len(i)>v:
#             v=len(i)
#     maxlen2=[]
#     for i in u:
#         if len(i)==v:
#             maxlen2.append(i)

#     sent_tokenize(data3)
#     token2=[word_tokenize(i) for i in sent_tokenize(data3)]
#     w=[]
#     for i in token2[0]:
#         if len(i)%2==0:
#             w.append(i)
    
#     #return (maxlen1[0])
#     return (maxlen2[0])
#     return (w)
#     return maxlen2[0]


    sent_tokenize(data1)
    tokens=[word_tokenize(i) for i in sent_tokenize(data1)]
    u=[]#list consisting of all even words
    for i in range(len(tokens)):
        for j in range(len(tokens[i])):
            if len(tokens[i][j])%2==0:
                u.append(tokens[i][j])
    v=0 #variable initialised to zero for calculating max length of even nos
    w=[]#list for storing final result of which we need the first element
    for i in u:
        if len(i)>v:
            v=len(i)
    for i in u:
        if len(i)==v:
            w.append(i)
    if len(w)!=0:#check if list is empty or not
        return w[0]
    else:
        return 0
            
    
    
    
    
    

    



data1='One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'

c=q01_longest_even_word(data1)
c
data1 = 'photographs or other images, readers can start to get a sense about the topic. This scanning and skimming helps set the expectation for the reading.'
c=q01_longest_even_word(data1)

c
data1 = ' testing very9 important'
c=q01_longest_even_word(data1)
c






