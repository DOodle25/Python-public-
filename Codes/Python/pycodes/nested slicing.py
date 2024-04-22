a = '*****'
b = "     "
len_ = len(a)
for i in range (len_):
        print(b[0:i],end=" ")
        print(a[1])
print()
for i in range (len_):
        print(b[len_:i:-1],end=" ")
        print(a[1])
print()
for i in range (len_):
        print(a[0:i+1])
print()
for i in range (len_):
        print(b[0:i],end=" ")
        print(a[0:len_-i])
print()
for i in range (len_):
        print(a[0:len_-i])
print()
for i in range (len_):
        print(b[0:len_-i-1],end=" ")
        print(a[0:i+1])
len_ = 10
if len_ % 2 == 0:
                len_ -= 1
for i in range (len_):
        for j in range (len_):
                if (i == 0 or j == 0 or i == len_-1 or j == len_-1 ):
                        print("#",end=" ")
                elif (i == (int(len_/2)) and j == (int(len_/2))):
                        print("#",end=" ")
                else:
                        print(" ",end=" ")
        print()
print()
for i in range (len_):
        for j in range (len_ - (i+1)):
                print(" ",end="")
        for k in range (i+1):
                print("#",end=" ")
        print()
print()
if len_ % 2 != 0:
        len_ += 1
for i in range (len_):
        if len_%2 == 0:
                for j in range (len_):
                        if (i == 0 or i == 1)and(j > ((len_/2))):
                                print("#",end=" ")
                        elif (j == len_-1 or j == len_ - 2) and (i > ((len_/2))):
                                print("#",end=" ")
                        elif (j == 0 or j == 1)and(i<((len_/2))):
                                print("#",end=" ")
                        elif (i == len_ - 1 or i == len_ - 2) and (j < ((len_/2))):
                                print("#",end=" ")
                        elif (j == (len_/2)) or (j == ((len_/2)-1)):
                                print("#",end=" ")
                        elif (i == (len_/2)) or (i == ((len_/2)-1)):
                                print("#",end=" ")
                        else:
                                print(" ",end=" ")
        else :
                len_-=1
                for j in range (len_):
                        if (i == 0 or i == 1)and(j > ((len_/2))):
                                print("#",end=" ")
                        elif (j == len_-1 or j == len_ - 2) and (i > ((len_/2))):
                                print("#",end=" ")
                        elif (j == 0 or j == 1)and(i<((len_/2))):
                                print("#",end=" ")
                        elif (i == len_ - 1 or i == len_ - 2) and (j < ((len_/2))):
                                print("#",end=" ")
                        elif (j == (len_/2)) or (j == ((len_/2)-1)):
                                print("#",end=" ")
                        elif (i == (len_/2)) or (i == ((len_/2)-1)):
                                print("#",end=" ")
                        else:
                                print(" ",end=" ")
                
        print()
print()       
 
n = int(input("S:"))
n |= 1
for i in range (n):
        for j in range (n):
                if(j == 0):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i == 0):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(j == n-1):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(j == 3*(n//4)):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(j == n//2):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(j == n //4):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i - j == 0):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i + j == n-1):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i == (n//4)+(n//2)):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i == n//2):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i == n//4):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i == n-1):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i+j == n//2):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i - j == -(n//2)):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i-j == n//2):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i+j == 3*(n//2)):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()

for i in range (n):
        for j in range (n):
                if(j == 0):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i == 0):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(j == n-1):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(j == 3*(n//4)):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(j == n//2):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(j == n //4):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i - j == 0):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i + j == n-1):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i == (n//4)+(n//2)):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i == n//2):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i == n//4):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i == n-1):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i+j == n//2):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i - j == -(n//2)):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i-j == n//2):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
for i in range (n):
        for j in range (n):
                if(i+j == 3*(n//2)):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()

for i in range (n):
        for j in range (n):
                if(j == 0):
                        print("#",end = " ")
                elif(i == 0):
                        print("#",end = " ")
                elif(j == n-1):
                        print("#",end = " ")
                elif(j == 3*(n//4)):
                        print("#",end = " ")
                elif(j == n//2):
                        print("#",end = " ")
                elif(j == n //4):
                        print("#",end = " ")
                elif(i - j == 0):
                        print("#",end = " ")
                elif(i + j == n-1):
                        print("#",end = " ")
                elif(i == (n//4)+(n//2)):
                        print("#",end = " ")
                elif(i == n//2):
                        print("#",end = " ")
                elif(i == n//4):
                        print("#",end = " ")
                elif(i == n-1):
                        print("#",end = " ")
                elif(i+j == n//2):
                        print("#",end = " ")
                elif(i - j == -(n//2)):
                        print("#",end = " ")
                elif(i-j == n//2):
                        print("#",end = " ")
                elif(i+j == 3*(n//2)):
                        print("#",end = " ")
                elif(j == 0):
                        print("#",end = " ")
                elif(i == 0):
                        print("#",end = " ")
                elif(j == n-1):
                        print("#",end = " ")
                elif(j == 3*(n//4)):
                        print("#",end = " ")
                elif(j == n//2):
                        print("#",end = " ")
                elif(j == n //4):
                        print("#",end = " ")
                elif(i - j == 0):
                        print("#",end = " ")
                elif(i + j == n-1):
                        print("#",end = " ")
                elif(i == (n//4)+(n//2)):
                        print("#",end = " ")
                elif(i == n//2):
                        print("#",end = " ")
                elif(i == n//4):
                        print("#",end = " ")
                elif(i == n-1):
                        print("#",end = " ")
                elif(i+j == n//2):
                        print("#",end = " ")
                elif(i - j == -(n//2)):
                        print("#",end = " ")
                elif(i-j == n//2):
                        print("#",end = " ")
                elif(i+j == 3*(n//2)):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
print()
for i in range (n):
        for j in range (n):
                if not (j == 0):
                        print(" ",end = " ")
                elif not(i == 0):
                        print(" ",end = " ")
                elif not(j == n-1):
                        print(" ",end = " ")
                elif not(j == 3*(n//4)):
                        print(" ",end = " ")
                elif not(j == n//2):
                        print(" ",end = " ")
                elif not(j == n //4):
                        print(" ",end = " ")
                elif not(i - j == 0):
                        print(" ",end = " ")
                elif not(i + j == n-1):
                        print(" ",end = " ")
                elif not(i == (n//4)+(n//2)):
                        print(" ",end = " ")
                elif not(i == n//2):
                        print(" ",end = " ")
                elif not(i == n//4):
                        print(" ",end = " ")
                elif not(i == n-1):
                        print(" ",end = " ")
                elif not(i+j == n//2):
                        print(" ",end = " ")
                elif not(i - j == -(n//2)):
                        print(" ",end = " ")
                elif not(i-j == n//2):
                        print(" ",end = " ")
                elif not(i+j == 3*(n//2)):
                        print(" ",end = " ")
                elif not(j == 0):
                        print(" ",end = " ")
                elif not(i == 0):
                        print(" ",end = " ")
                elif not(j == n-1):
                        print(" ",end = " ")
                elif not(j == 3*(n//4)):
                        print(" ",end = " ")
                elif not(j == n//2):
                        print(" ",end = " ")
                elif not(j == n //4):
                        print(" ",end = " ")
                elif not(i - j == 0):
                        print(" ",end = " ")
                elif not(i + j == n-1):
                        print(" ",end = " ")
                elif not(i == (n//4)+(n//2)):
                        print(" ",end = " ")
                elif not(i == n//2):
                        print(" ",end = " ")
                elif not(i == n//4):
                        print(" ",end = " ")
                elif not(i == n-1):
                        print(" ",end = " ")
                elif not(i+j == n//2):
                        print(" ",end = " ")
                elif not(i - j == -(n//2)):
                        print(" ",end = " ")
                elif not(i-j == n//2):
                        print(" ",end = " ")
                elif not(i+j == 3*(n//2)):
                        print(" ",end = " ")
                else:
                        print("#",end = " ")
        print()

m = int(input("S:"))
m |= 1
for i in range (m):
        for j in range (m):
                if((i >= 3*(n//4)) and (j <= (n//2)) and (i-j)<=(n//2)):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
print()
for i in range (m):
        for j in range (m):
                if((i >= 3*(n//4)) and (j <= (n//2)) and (i-j)<=(n//3)):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
print()
for i in range (m):
        for j in range (m):
                if(i<=(n//4))and(j>=(3*(n//4))):
                        print("#",end = " ")
                elif(i<=(n//4))and(j<=((n//4))):
                        print("#",end = " ")
                else:
                        print(" ",end = " ")
        print()
print()