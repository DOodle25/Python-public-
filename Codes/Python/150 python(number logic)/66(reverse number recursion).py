def reverse_number_recursive(number):
    if number < 10:
        return number
    else:
        return int(str(number % 10) + str(reverse_number_recursive(number // 10)))

print(reverse_number_recursive(int(input("X:"))))

