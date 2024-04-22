def spiral(n):
    a=(n-1)*4+1
   
    for i in range(n):
        for j in range(n):
             b=((j*n)-j*(j+2))*4+j
             if i==0:
                 print(j+1,end='  ')
             elif i>=1 and j==0:
                 print(a-i,end=' ')
             elif i==n//2 and j==n//2:
                 print(n**2,end=' ')
             elif j==n-1:
                 print(n+i,end='  ')
             elif i==n-1:
                 print(a-i-j,end=' ')
             elif i-j<=0 and i+j<=n-1:
                 print((a-i)+j+(((i-1)*n)-(i-1)*(i+1))*4,end=' ')
             elif j<=i-1 and j<(n//2) and i+j<n:
                 print((a-i)+b,end=' ')
             elif i-j<=0 and i+j>=n-1 and j>=n//2:
                 print(n**2-((j-n//2)*(4*(j-n//2)+1))-(n//2-i),end=' ')
             else:
                 print((a-i)-j+(((i-1)*n)-(i-1)*(i+1))*4+(n-i-1)*2,end=" ")
        print()

spiral(6)