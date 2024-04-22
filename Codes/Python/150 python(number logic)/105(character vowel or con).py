def VowelOrConsonant(c): 
    if(c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'):
        print(f"{c} is Vowel") 
    else: 
        print(f"{c} is Consonant") 
c = 'D'
print(c)
VowelOrConsonant(c)