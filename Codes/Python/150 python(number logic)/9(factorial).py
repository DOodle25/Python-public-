def factorial(n):
    sum = 1
    if (n == 1):
        return 1
    for i in range (2,n+1):
        sum = sum * i
    return sum

print(factorial(int(input("Enter the num ber for facorial counting:"))))