def pwr(b,p): 
    if(p==1): 
        return(b) 
    if(p!=1): 
        return(b*pwr(b,p-1)) 
        
b=int(input("Enter base: ")) 
p=int(input("Enter exponential value: ")) 
print(pwr(b,p))