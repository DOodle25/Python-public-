# Range()

The `range()` function in Python is used to generate a sequence of numbers. It's often used in conjunction with loops, especially `for` loops, to iterate a certain number of times. The `range()` function can be called with one, two, or three arguments:

1. `range(stop)`: Generates a sequence of numbers from `0` to `stop - 1`.
2. `range(start, stop)`: Generates a sequence of numbers from `start` to `stop - 1`.
3. `range(start, stop, step)`: Generates a sequence of numbers from `start` to `stop - 1` with the specified step size.

Now, let's dive into examples of using the `range()` function with and without `for` loops:

### Using `range()` with a `for` Loop:

```python
# Example 1: Generating numbers from 0 to 4
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# Example 2: Generating numbers from 2 to 6
for i in range(2, 7):
    print(i)
# Output:
# 2
# 3
# 4
# 5
# 6

# Example 3: Generating even numbers from 0 to 10
for i in range(0, 11, 2):
    print(i)
# Output:
# 0
# 2
# 4
# 6
# 8
# 10
```

In these examples, the `range()` function generates a sequence of numbers according to the specified parameters, and the `for` loop iterates over each number in the sequence, printing it to the console.

### Using `range()` without a `for` Loop:

While the `range()` function is commonly used with `for` loops, you can also use it to generate a sequence of numbers and convert it to other data types like a list or tuple.

```python
# Example 1: Generating a list of numbers from 0 to 4
numbers_list = list(range(5))
print(numbers_list)  # Output: [0, 1, 2, 3, 4]

# Example 2: Generating a tuple of numbers from 2 to 6
numbers_tuple = tuple(range(2, 7))
print(numbers_tuple)  # Output: (2, 3, 4, 5, 6)

# Example 3: Generating a set of even numbers from 0 to 10
numbers_set = set(range(0, 11, 2))
print(numbers_set)  # Output: {0, 2, 4, 6, 8, 10}
```

In these examples, the `range()` function generates a sequence of numbers, and then it's converted to a list, tuple, or set using the appropriate constructor (`list()`, `tuple()`, `set()`). This can be useful when you need a collection of numbers for further processing or manipulation.

Overall, the `range()` function is a powerful tool in Python for generating sequences of numbers, which can be used in various scenarios, especially for controlling loops and generating lists of numbers.