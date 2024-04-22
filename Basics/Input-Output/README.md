# Input Output

**1. Input/Output (I/O)**:
Input/output operations in Python are used to interact with the user through the command line or to read from and write to files.

- **Input**: The `input()` function is used to take input from the user. It reads a line of text from the standard input (keyboard) and returns it as a string.

Example:
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

- **Output**: The `print()` function is used to display output to the console. It can take multiple arguments separated by commas and prints them to the console with a space between each argument.

Example:
```python
print("Hello", "world!")
```

**2. f-strings**:
f-strings, also known as formatted string literals, provide a concise and readable way to format strings in Python. They allow you to embed expressions inside string literals, which are replaced with their values.

Example:
```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

**3. format() method**:
The `format()` method is another way to format strings in Python. It allows you to insert variables or values into a string by specifying placeholders and providing values to replace them.

Example:
```python
name = "Bob"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message)
```

Both f-strings and the `format()` method provide powerful string formatting capabilities, but f-strings are generally considered more concise and easier to read.
