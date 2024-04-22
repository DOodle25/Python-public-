def decimal_binary(n):
    if n == 0:
        print(0,end="")
        return
    elif n == 1:
        print(1,end="")
        n = 0
        return
    else:
        decimal_binary(n//2)
        print(n%2,end="")
        return
while(True):
    decimal_binary(int(input("N:")))