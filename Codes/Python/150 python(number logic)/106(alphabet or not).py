def Alphabet(c): 
    if c>='a' and c<='z': 
        return True
    elif c>='A' and c<='z':
        return True
    else: 
        return False 
c = 'D'
print(Alphabet(c))