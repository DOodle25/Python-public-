def lcm(n,m):
    if n==m:
        return n
    if n < m :
        lcm = 1
        for i in range(m,(m*n)+1,m):
            if(i%n == 0 and i%m == 0):
                return i
    else:
        lcm = 1
        for i in range(n,(m*n)+1,n):
            if(i%n == 0 and i%m == 0):
                return i

print(lcm(int(input("X:")),int(input("Y:"))))