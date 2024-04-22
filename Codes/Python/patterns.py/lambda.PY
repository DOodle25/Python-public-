reference = {
    'A': lambda i, j: '*' if (j == 0 or j == n-1 or (i == 0 or i == n//2) and (j > 0 and j < n-1)) else ' ',
    'B': lambda i, j: '*' if (j == 0 or (i == 0 or i == n-1 or i == n//2) and j < n-1 and j > 0) or (j == n-1 and i != 0 and i != n-1 and i != n//2) else ' ',
    'C': lambda i, j: '*' if (j == 0 and i != 0 and i != n-1) or ((i == 0 or i == n-1) and j > 0) else ' ',
    'D': lambda i, j: '*' if (j == 0 or (j == n-1 and i != 0 and i != n-1) or (i == 0 or i == n-1) and j < n-1) else ' ',
    'E': lambda i, j: '*' if (j == 0 or (i == 0 or i == n-1 or i == n//2) and j < n-1) else ' ',
    'F': lambda i, j: '*' if (j == 0 or (i == 0 or i == n//2) and j < n-1) else ' ',
    'G': lambda i, j: '*' if (j == 0 and i != 0 and i != n-1) or ((i == 0 or i == n-1) and j > 0) or (i == n-1 and j > n//2) or (j == n-1 and i > n//2) else ' ',
    'H': lambda i, j: '*' if (j == 0 or j == n-1 or i == n//2) else ' ',
    'I': lambda i, j: '*' if (i == 0 or i == n-1 or j == n//2) else ' ',
    'J': lambda i, j: '*' if (i == 0 or (j == n//2 and i != n-1) or (i == n-1 and j <= n//2)) else ' ',
    'K': lambda i, j: '*' if (j == 0 or (i+j == n//2) or (j == n-1 and i+j >= n//2*3)) else ' ',
    'L': lambda i, j: '*' if (j == 0 or i == n-1) else ' ',
    'M': lambda i, j: '*' if (j == 0 or j == n-1 or (i == j and j < n//2) or (i+j == n-1 and j >= n//2)) else ' ',
    'N': lambda i, j: '*' if (j == 0 or j == n-1 or i == j) else ' ',
    'O': lambda i, j: '*' if (j == 0 or j == n-1 or i == 0 or i == n-1) else ' ',
    'P': lambda i, j: '*' if (j == 0 or (i == 0 or i == n//2) and j < n-1) or (j == n-1 and i < n//2) else ' ',
    'Q': lambda i, j: '*' if (j == 0 or j == n-1 or i == 0 or i == n-1 or (i >= n//2 and j >= n//2)) else ' ',
    'R': lambda i, j: '*' if (j == 0 or (i == 0 or i == n//2) and j < n-1) or (j == n-1 and i != 0 and i != n//2) or (i-j == 0 and j >= n//2) else ' ',
    'S': lambda i, j: '*' if ((i == 0 or i == n-1 or i == n//2) and j > 0 and j < n-1) or (j == 0 and i < n//2) or (j == n-1 and i > n//2) else ' ',
    'T': lambda i, j: '*' if (i == 0 or j == n//2) else ' ',
    'U': lambda i, j: '*' if ((j == 0 or j == n-1) and i != n-1) or (i == n-1 and j > 0 and j < n-1) else ' ',
    'V': lambda i, j: '*' if ((i < n//2 and j == i) or (i < n//2 and j == n-i-1) or (i >= n//2 and j == n//2)) else ' ',
    'W': lambda i, j: '*' if ((j == 0 or j == n-1) or (i >= n//2 and (i == j or i+j == n-1))) else ' ',
    'X': lambda i, j: '*' if (i == j or i+j == n-1) else ' ',
    'Y': lambda i, j: '*' if ((i < n//2 and j == i) or (i < n//2 and j == n-i-1) or (i >= n//2 and j == n//2)) or (i == n-1 and j == n//2) else ' ',
    'Z': lambda i, j: '*' if (i == 0 or i == n-1 or i+j == n-1) else ' ',

    '0': lambda i, j: '*' if (i == 0 or i == n-1 or j == 0 or j == n-1) else ' ',
    '1': lambda i, j: '*' if (j == n//2 or i == n-1) else ' ',
    '2': lambda i, j: '*' if ((i == 0 or i == n-1) and j < n-1) or (j == n-1 and i > 0 and i < n//2) or (i == n//2) else ' ',
    '3': lambda i, j: '*' if (j == n-1 or (i == 0 or i == n-1 or i == n//2) and j < n-1) else ' ',
    '4': lambda i, j: '*' if (j == 0 or (i == 0 or i == n//2) and j < n-1) or (j == n-1 and i > n//2) else ' ',
    '5': lambda i, j: '*' if ((i == 0 or i == n-1) and j < n-1) or (j == 0 and i < n//2) or (j == n-1 and i > n//2) or (i == n//2) else ' ',
    '6': lambda i, j: '*' if (j == 0 and i > 0 and i < n-1) or ((i == 0 or i == n-1) and j < n-1) or (j == n-1 and i >= n//2) or (i == n//2) else ' ',
    '7': lambda i, j: '*' if (i == 0 or j == n-1) else ' ',
    '8': lambda i, j: '*' if (j == 0 or j == n-1 or i == 0 or i == n-1 or i == n//2) else ' ',
    '9': lambda i, j: '*' if (j == 0 or (i == 0 or i == n//2) and j < n-1) or (j == n-1 and i > n//2) else ' ',
}

def print_pattern(character, size):
    global n
    n = size
    for i in range(n):
        for j in range(n):
            print(reference[character](i, j), end=' ')
        print()

# Example usage for the letter 'E' with size 5
print_pattern('B', 20)

# Example usage for the number '5' with size 5

