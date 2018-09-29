def q01_longest_even_word(sentence):
    
    str1 = sentence.split()
    str2 = list(filter(lambda x: len(x)%2==0,str1))
    output = max(str2, key=len) if str2 else 0
    
    return output

sentence = 'y nam i Bhavesh'
q01_longest_even_word(sentence)


        
        
        
    


