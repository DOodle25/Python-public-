def decimal_binary(n):
        if (n < 2):
            return n
        else:
            return n % 2 + 10 * (decimal_binary(n // 2))

while True:
    print(decimal_binary(int(input("B:"))))