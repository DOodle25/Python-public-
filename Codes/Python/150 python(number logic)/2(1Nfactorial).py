def one_upon_factorial(n):
    sum = 1
    if (n == 1):
        return 1
    for i in range (2,n+1):
        sum = sum * i
    return 1/sum

print(one_upon_factorial(int(input("Enter the number for facorial counting:"))))