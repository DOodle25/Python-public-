# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
i = int(1)
while(i != n):
    tnum = int(i)
    tsum = int(i)
    for j in range(1,i):
        tsum = tsum + (tnum *(10 ** j))
    print(tsum)
    i += 1
    

