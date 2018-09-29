#%load q01_longest_even_word/build.py


def q01_longest_even_word(Str):
#Str='my1 nam iss Aji'

    list=Str.split()

    l3=[items for items in list if len(items)%2==0]
    if len(l3)>0:
        l2=max(l3, key=len)
    else:
        l2=0
    
#print(l2)

    return l2


q01_longest_even_word('my1 nam iss Ajit')









