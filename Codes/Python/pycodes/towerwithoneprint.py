# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(1,n):
    s = int(i)
    for j in range(1,i):
        tnum = int(i)
        for k in range(0,j):
            tnum = tnum * 10
        s = s + tnum
    print(s)
