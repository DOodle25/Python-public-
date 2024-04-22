def length_of_int(n):
        n = n
        i = int(0)
        if n == 0:
            return 1
        if n < 0:
            n *= -1
        while n:
            n //= 10
            i += 1
        return i
def print_reverse(k):
    if k == 0:
        return 
    else:
        print_reverse(k//10)
        print(k%10, end = " ")
def factorial(n):
    sum = 1
    if (n == 1):
        return 1
    for i in range (2,n+1):
        sum = sum * i
    return sum
def p92(n):
    n = n | 1
    for i in range(n):
        for j in range(n - 1 - i , 0 , -1):
            print(" ", end = "") 
        for j in range(i+1):
            print(int((factorial(i)/(factorial(j)*(factorial(i-j))))), end = " ")
        print()

p92(int(input("N: ")))  