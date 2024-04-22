def hcf(n,m):
    if n < m :
        hcf = 1
        for i in range(1,n+1):
            print(i)
            if(n%i == 0 and m%i == 0):
                hcf = i 
    else:
        hcf = 1
        for i in range(1,m+1):
            if(n%i == 0 and m%i == 0):
                hcf = i 
    return hcf

print(hcf(int(input("X:")),int(input("Y:"))))