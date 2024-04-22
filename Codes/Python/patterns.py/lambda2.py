def print_pattern(char, size):
    patterns = {
        'A': lambda i, j: '•' if (j == 0 or j == size - 1) or (i == 0 or i == size // 2) or (i > 0 and j > 0 and i < size // 2 and j < size - 1 and i == j) or (i > 0 and j > 0 and i < size // 2 and j < size - 1 and i + j == size - 1) else ' ',
        'B': lambda i, j: '•' if (j == 0 or (i == 0 or i == size - 1 or i == size // 2) and j < size - 1) or (i > 0 and i < size // 2 and j == size - 1) or (i > size // 2 and i < size - 1 and j == size - 1) else ' ',
        'C': lambda i, j: '•' if (j == 0 and i > 0 and i < size - 1) or (i == 0 or i == size - 1) and j > 0 else ' ',
        '1': lambda i, j: '•' if j == size // 2 or (i == 0 and j > 0 and j < size) or (i == size - 1 and j > 0 and j < size) else ' ',
        '2': lambda i, j: '•' if (i == 0 or i == size // 2 or i == size - 1) or (i < size // 2 and j == size - 1) or (i > size // 2 and j == 0) else ' ',
        # Add more characters as needed
    }

    if char in patterns:
        pattern = patterns[char]
        for i in range(size):
            for j in range(size):
                print(pattern(i, j), end=' ')
            print()
    else:
        print("Character not supported.")

# Example usage:
print_pattern('A', 20)
print_pattern('B', 5)
print_pattern('C', 5)
print_pattern('1', 5)
print_pattern('2', 5)
