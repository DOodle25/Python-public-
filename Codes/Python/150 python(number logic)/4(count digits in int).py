def length_of_int(n):
        num = n
        i = int(0)
        if num == 0:
            return 1
        if num < 0:
            num *= -1
        while num:
            num //= 10
            i += 1
        return i
print(length_of_int(int(input("Enter the number:"))))