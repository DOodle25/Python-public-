a = []
input_ = [int(j) for j in input().split()]
print(input_)
j = 0
for i in input_:
    a.append(i)
    k = j
    while True:
        if (k - 1) // 2 < 0:
            break
        elif a[(k - 1) // 2] < a[k]:
            a[(k - 1) // 2], a[k] = a[k], a[(k - 1) // 2]
            k = (k - 1) // 2
        else:
            break
    j += 1
    print(a)
k = 0
for i in range(len(a) - 1, 1, -1):
    a[i], a[0] = a[0], a[i]
    a = a[:-1]
    print(a)
    while True:
        k = 0
        if ((k * 2) + 1) >= i or ((k * 2) + 2) >= i:
            break
        elif (a[(k * 2) + 1] > a[k] or a[(k * 2) + 2] > a[k]):
            if a[(k * 2) + 1] > a[(k * 2) + 2]:
                a[(k * 2) + 1], a[k] = a[k], a[(k * 2) + 1]
                k = (k * 2) + 1
            else:
                a[(k * 2) + 2], a[k] = a[k], a[(k * 2) + 2]
                k = (k * 2) + 2
        else:
            break
if a[0] < a[1]:
    a = a[:-1]
else:
    a[0], a[1] = a[1], a[0]
    a = a[:-1]
print(a)
