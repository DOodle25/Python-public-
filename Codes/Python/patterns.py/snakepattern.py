height , length = 4 , 65
k = height + 1
for i in range(height):
    o = height - i
    for k in range (height - i):
        print(" ",end = " ")
    if i == 0 or i == height -1:
        gap1,gap2 = height + 1, height + 1
    else :
        k = -1
        l = -1
        for n in range(height - i -1):
            l += 2
        for m in range(i):
            k += 2
        gap1,gap2 = k+1,l
    s_gap = 1
    for j in range(height-i - 1,length):
        if j == 0:
            print(0,end = " ")
        elif i == height-1 and j == 1:
            print(" ",end = " ")
        elif((j+1)%(o) == 0):
            print(j,end = " ")
            if s_gap == 0:
                o += gap2
                s_gap = 1
            else :
                o += gap1
                s_gap = 0
        else:
            print(" ",end = " ") 
    print()
    