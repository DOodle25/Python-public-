# built-in String Functions

1. **count(substring)**: This method returns the number of occurrences of a substring within the string.

```python
string = "hello world"
print(string.count('l'))  # Output: 3
```

2. **index(substring)**: Returns the index of the first occurrence of a substring in the string. Raises a ValueError if the substring is not found.

```python
string = "hello world"
print(string.index('o'))  # Output: 4
```

3. **find(substring)**: Similar to index(), but returns -1 if the substring is not found instead of raising an exception.

```python
string = "hello world"
print(string.find('o'))  # Output: 4
print(string.find('z'))  # Output: -1
```

4. **startswith(prefix)**: Returns True if the string starts with the specified prefix; otherwise, returns False.

```python
string = "hello world"
print(string.startswith('hello'))  # Output: True
```

5. **endswith(suffix)**: Returns True if the string ends with the specified suffix; otherwise, returns False.

```python
string = "hello world"
print(string.endswith('world'))  # Output: True
```

6. **isdigit()**: Returns True if all characters in the string are digits; otherwise, returns False.

```python
string = "12345"
print(string.isdigit())  # Output: True
```

7. **isalpha()**: Returns True if all characters in the string are alphabetic; otherwise, returns False.

```python
string = "hello"
print(string.isalpha())  # Output: True
```

8. **isalnum()**: Returns True if all characters in the string are alphanumeric (letters or numbers); otherwise, returns False.

```python
string = "hello123"
print(string.isalnum())  # Output: True
```

9. **isidentifier()**: Returns True if the string is a valid Python identifier; otherwise, returns False.

```python
string = "hello_world"
print(string.isidentifier())  # Output: True
```

10. **upper()**: Returns a copy of the string converted to uppercase.

```python
string = "hello world"
print(string.upper())  # Output: HELLO WORLD
```

11. **lower()**: Returns a copy of the string converted to lowercase.

```python
string = "HELLO WORLD"
print(string.lower())  # Output: hello world
```

12. **title()**: Returns a copy of the string with the first character of each word capitalized.

```python
string = "hello world"
print(string.title())  # Output: Hello World
```

13. **isupper()**: Returns True if all characters in the string are uppercase; otherwise, returns False.

```python
string = "HELLO"
print(string.isupper())  # Output: True
```

14. **islower()**: Returns True if all characters in the string are lowercase; otherwise, returns False.

```python
string = "hello"
print(string.islower())  # Output: True
```

15. **istitle()**: Returns True if the string is titlecased (all words start with uppercase letters, and the rest are lowercase); otherwise, returns False.

```python
string = "Hello World"
print(string.istitle())  # Output: True
```

16. **capitalize()**: Returns a copy of the string with the first character capitalized and the rest lowercase.

```python
string = "hello world"
print(string.capitalize())  # Output: Hello world
```

17. **split(separator)**: Splits the string into a list of substrings based on the specified separator.

```python
string = "hello,world"
print(string.split(','))  # Output: ['hello', 'world']
```

18. **join(iterable)**: Concatenates the elements of an iterable (e.g., list) into a single string, using the string as a separator.

```python
words = ['hello', 'world']
print(' '.join(words))  # Output: hello world
```

19. **replace(old, new)**: Returns a copy of the string with all occurrences of the old substring replaced by the new substring.

```python
string = "hello world"
print(string.replace('world', 'universe'))  # Output: hello universe
```

20. **format()**: Formats the string with the specified values.

```python
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Alice and I am 30 years old.
```

Now, let's discuss slicing:

Slicing allows you to extract a portion of a string using indices. The syntax is `string[start:stop:step]`.

- **start**: The index where the slicing starts (inclusive).
- **stop**: The index where the slicing ends (exclusive).
- **step**: The step value for slicing (optional, default is 1).

```python
string = "hello world"
print(string[0:5])   # Output: hello
print(string[6:])    # Output: world
print(string[:5])    # Output: hello
print(string[::-1])  # Output: dlrow olleh (reversed string)
```


## Input behaviours:

1. **count(substring)**:
   - If the input string is `None`, `0`, or `-1`, it will raise a `TypeError` because these values are not valid strings.

2. **index(substring)**:
   - If the substring is not found, it will raise a `ValueError`. If the input string is `None`, `0`, or `-1`, it will raise a `TypeError`.

3. **find(substring)**:
   - If the substring is not found, it will return `-1`. If the input string is `None`, `0`, or `-1`, it will raise a `TypeError`.

4. **startswith(prefix)**:
   - If the input string is `None`, `0`, or `-1`, it will raise a `TypeError`.

5. **endswith(suffix)**:
   - If the input string is `None`, `0`, or `-1`, it will raise a `TypeError`.

6. **isdigit()**:
   - If the input string is `None`, `0`, or `-1`, it will return `False` because they are not valid strings.

7. **isalpha()**:
   - If the input string is `None`, `0`, or `-1`, it will return `False` because they are not valid strings.

8. **isalnum()**:
   - If the input string is `None`, `0`, or `-1`, it will return `False` because they are not valid strings.

9. **isidentifier()**:
   - If the input string is `None`, `0`, or `-1`, it will return `False` because they are not valid strings.

10. **upper()**:
    - If the input string is `None`, `0`, or `-1`, it will raise a `TypeError`.

11. **lower()**:
    - If the input string is `None`, `0`, or `-1`, it will raise a `TypeError`.

12. **title()**:
    - If the input string is `None`, `0`, or `-1`, it will raise a `TypeError`.

13. **isupper()**:
    - If the input string is `None`, `0`, or `-1`, it will return `False` because they are not valid strings.

14. **islower()**:
    - If the input string is `None`, `0`, or `-1`, it will return `False` because they are not valid strings.

15. **istitle()**:
    - If the input string is `None`, `0`, or `-1`, it will return `False` because they are not valid strings.

16. **capitalize()**:
    - If the input string is `None`, `0`, or `-1`, it will raise a `TypeError`.

17. **split(separator)**:
    - If the input string is `None`, `0`, or `-1`, it will raise a `TypeError`.

18. **join(iterable)**:
    - If the input iterable is `None`, `0`, or `-1`, it will raise a `TypeError`.

19. **replace(old, new)**:
    - If the input string is `None`, `0`, or `-1`, it will raise a `TypeError`.

20. **format()**:
    - If the input string is `None`, `0`, or `-1`, it will raise a `TypeError`.
