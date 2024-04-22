def X_upon_factorial(num,power):
    number = num
    pwr = power
    if pwr == 0:
        num = 1
    else :
        while pwr != 1:
            number *=  num
            pwr -= 1
    print(number)
    sum = 1
    if (power == 1):
        sum = 1
    for i in range (2,power+1):
        sum = sum * i
    print(sum)
    return (1/sum)*number

print(X_upon_factorial(int(input("Enter the value of X:")),int(input("Enter the number for facorial counting:"))))