def spiral(n):
    for i in range(0, n):
        for j in range(0, n):
            f = 0
            l = min(i, j, n - i - 1, n - j - 1)
            for k in range(l):
                f = f + 4 * (n - l)
            if (j - i >= 0):
                if (i + j > n - 1):
                    print(f"{(f + i - l + (n - l * 2)):2}", end=" ")
                else:
                    print(f"{f + j - l + 1:2}", end=" ")
            else:
                if not i + j < n - 1:
                    print(f"{f + i - j + 2 * (n - l * 2) - 1:2}", end=" ")
                else:
                    print(f"{f + (n -j - i - 1) + (n - l - 1 - j) + 2 *(n - l * 2) - 1:2}", end=" ")
        print()
while(True):
    spiral(int(input()))