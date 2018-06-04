def q01_longest_even_word(s):
    l = s.split()
    
    new_s = ''
    len_s = 0
    
    for i in l:
        if len(i) % 2 == 0:
            if len(i) > len_s:
                new_s = i
                len_s = len(i)
            
    if new_s != '':
        return new_s
    else:
        return 0


