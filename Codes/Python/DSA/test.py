def spiral(n):
    for i in range(0, n):
        for j in range(0, n):
            f = 0
            l = min(i, j, n - i - 1, n - j - 1)
            #layer value
            for k in range(l):
                f = f + 4 * (n - l)
            #four side conditions
            if (j - i >= 0):
                if (i + j > n - 1):
                    print(f"{(f + i - l + (n - l * 2)):3}", end=" ")
                else:
                    print(f"{f + j - l + 1:3}", end=" ")
            else:
                if not i + j < n - 1:
                    print(f"{f + i - j + 2 * (n - l * 2) - 1:3}", end=" ")
                else:
                    print(f"{f + (n -j - i - 1) + (n - l - 1 - j) + 2 *(n - l * 2) - 1:3}", end=" ")
        print()
#using comprehension 
def spiral_in_one(n):
    [[(print(f"{(sum(4 * (n - min(i, j, n - i - 1, n - j - 1)) for k in range(min(i, j, n - i - 1, n - j - 1))) + i - min(i, j, n - i - 1, n - j - 1) + (n - min(i, j, n - i - 1, n - j - 1) * 2)):3}",end=" ") if (i + j > n - 1) else print(f"{sum(4 * (n - min(i, j, n - i - 1, n - j - 1)) for k in range(min(i, j, n - i - 1, n - j - 1))) + j - min(i, j, n - i - 1, n - j - 1) + 1:3}", end=" ")) if (j - i >= 0) else (print(f"{sum(4 * (n - min(i, j, n - i - 1, n - j - 1)) for k in range(min(i, j, n - i - 1, n - j - 1))) + i - j + 2 * (n - min(i, j, n - i - 1, n - j - 1) * 2) - 1:3}",end=" ") if not i + j < n - 1 else print(f"{sum(4 * (n - min(i, j, n - i - 1, n - j - 1)) for k in range(min(i, j, n - i - 1, n - j - 1))) + (n - j - i - 1) + (n - min(i, j, n - i - 1, n - j - 1) - 1 - j) + 2 * (n - min(i, j, n - i - 1, n - j - 1) * 2) - 1:3}",end=" ")) for j in range (n)] and (print()) for i in range (n)]

while(True):
    spiral(int(input()))
    spiral_in_one(int(input()))