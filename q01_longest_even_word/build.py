# %load q01_longest_even_word/build.py
# Default imports

import re
from nltk.tokenize import word_tokenize
import pandas as pd


# Write your solution here :
def q01_longest_even_word(sentence):
    lst=sentence.split(' ')
    lst1=[word for word in lst if len(word)%2==0]
    if(lst1[0]==''):
        output=0
    else:
        df=pd.DataFrame(lst1)
        df['count']=df.iloc[:,0].apply(lambda x : len(x))
        output=df.sort_values(['count'], axis=0, ascending=False, inplace=False).iloc[0,0]
    return output


