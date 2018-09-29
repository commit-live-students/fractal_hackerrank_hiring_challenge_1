# %load q01_longest_even_word/build.py
# Default imports

# Write your solution here :
def q01_longest_even_word(sentence):
    a=[x for x in sentence.split() if len(x)%2==0]
    if a: 
        return max(a,key=len)
    else: 
        return 0

#For sentence having even string
q01_longest_even_word('Hi I am Vivek Shingate')

#For sentence having odd strings
#q01_longest_even_word('Hello I ain\'t Vivek Shingates')
    
    




