# Exception Handling

**1. Syntax Errors**:
Syntax errors occur when the Python parser encounters code that violates the language syntax rules. These errors prevent the code from being compiled or interpreted.

Example:
```python
print("Hello, world!)
```
Output:
```
SyntaxError: EOL while scanning string literal
```

**2. Exceptions**:
Exceptions are runtime errors that occur during the execution of a Python program. These errors disrupt the normal flow of the program and may cause it to terminate prematurely if not handled properly.

**3. Handling Exceptions**:
Exceptions can be handled using try-except blocks. The code inside the try block is executed, and if an exception occurs, it is caught and handled in the except block.

Example:
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

**4. Raising Exceptions**:
You can raise exceptions using the raise statement to signal that an error has occurred in your code.

Example:
```python
x = -1
if x < 0:
    raise ValueError("x cannot be negative")
```

**5. Exception Chaining**:
Exception chaining allows one exception to raise another, while maintaining the original traceback information.

Example:
```python
try:
    f = open('file.txt', 'r')
except IOError as e:
    raise RuntimeError("Failed to open file") from e
```

**6. User-defined Exceptions**:
You can create your own custom exceptions by subclassing the built-in Exception class.

Example:
```python
class MyError(Exception):
    pass

raise MyError("An error occurred")
```

**7. Defining Clean-up Actions**:
You can use the try-finally block to ensure that certain actions (such as closing files or releasing resources) are always executed, even if exceptions occur.

Example:
```python
try:
    f = open('file.txt', 'r')
    # Perform operations
finally:
    f.close()
```

**8. Predefined Clean-up Actions**:
Python provides the `with` statement, which automatically calls the `__enter__` and `__exit__` methods of an object, allowing for easy resource management.

Example:
```python
with open('file.txt', 'r') as f:
    # Perform operations
```

**9. Raising and Handling Multiple Unrelated Exceptions**:
You can handle multiple exceptions by listing them in a tuple inside the except block.

Example:
```python
try:
    # Code that may raise exceptions
except (ValueError, TypeError):
    # Handle exceptions
```

**10. Enriching Exceptions with Notes**:
You can attach additional information to exceptions using the `with_traceback()` method.

Example:
```python
try:
    # Code that may raise exceptions
except Exception as e:
    raise RuntimeError("An error occurred") from e
```

## built-in Exceptions

1. **SyntaxError**:
   - Raised when the Python parser encounters a syntax error in the code.

```python
print("Hello, world!)
```

2. **IndentationError**:
   - Raised when there is incorrect indentation in the code.

```python
def my_function():
print("Indented incorrectly")
```

3. **NameError**:
   - Raised when a local or global name is not found.

```python
print(unknown_variable)
```

4. **TypeError**:
   - Raised when an operation or function is applied to an object of an inappropriate type.

```python
result = 10 / '2'
```

5. **ValueError**:
   - Raised when a function receives an argument of the correct type but an inappropriate value.

```python
int('abc')
```

6. **ZeroDivisionError**:
   - Raised when division or modulo operation is performed with zero as the divisor.

```python
result = 10 / 0
```

7. **FileNotFoundError**:
   - Raised when a file or directory is requested but cannot be found.

```python
with open('non_existent_file.txt', 'r') as f:
    content = f.read()
```

8. **IndexError**:
   - Raised when a sequence subscript (e.g., list, tuple) is out of range.

```python
my_list = [1, 2, 3]
print(my_list[5])
```

9. **KeyError**:
   - Raised when a dictionary key is not found in the set of existing keys.

```python
my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])
```

10. **AttributeError**:
    - Raised when an attribute reference or assignment fails.

```python
x = 5
print(x.foo)
```
