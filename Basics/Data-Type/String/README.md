# String

**In Python, a string is a sequence of characters enclosed within either single quotes ('') or double quotes (""). Strings are immutable, meaning once they are created, their contents cannot be changed.**

- **Character Encoding**: Python strings are Unicode by default, which means they can represent any character from any language worldwide.

- **Indexing**: Strings can be accessed using indexing. Each character in the string has a unique index starting from 0 for the first character, 1 for the second character, and so on. Negative indices can also be used to access characters from the end of the string, with -1 representing the last character.

```python
string = "hello"
print(string[0])    # Output: h
print(string[-1])   # Output: o
```

- **Concatenation**: Strings can be concatenated using the `+` operator.

```python
string1 = "hello"
string2 = "world"
result = string1 + " " + string2
print(result)   # Output: hello world
```

- **Length**: The `len()` function can be used to find the length of a string, i.e., the number of characters it contains.

```python
string = "hello"
print(len(string))   # Output: 5
```

- **Iteration**: Strings can be iterated over using loops.

```python
string = "hello"
for char in string:
    print(char)
# Output:
# h
# e
# l
# l
# o
```

- **Escape Sequences**: Escape sequences are used to represent special characters within strings. Some common escape sequences include `\n` (newline), `\t` (tab), and `\\` (backslash).

```python
string = "hello\nworld"
print(string)
# Output:
# hello
# world
```

- **Raw Strings**: Raw strings are preceded by an 'r' or 'R' and treat backslashes as literal characters rather than escape characters.

```python
raw_string = r"C:\Users\John"
print(raw_string)   # Output: C:\Users\John
```

- **String Operations**: Various string operations can be performed, such as checking for substrings, checking if a string starts or ends with a particular substring, converting case, and more, which we discussed earlier.

- **String Methods**: Python provides a rich set of built-in string methods to manipulate and work with strings efficiently. These methods include `split()`, `join()`, `replace()`, `find()`, `count()`, `strip()`, `lower()`, `upper()`, `startswith()`, `endswith()`, and many more.

- **String Formatting**: Python supports multiple ways to format strings, including using the `format()` method, f-strings (formatted string literals), and the `%` operator.

- **String Comparison**: Strings can be compared using standard comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`), which compare strings lexicographically based on their Unicode code points.

```python
string1 = "hello"
string2 = "world"
print(string1 < string2)  # Output: True
```

- **String Slicing**: As mentioned earlier, slicing allows you to extract substrings from a string by specifying a range of indices.

Python strings are fundamental data types in Python and are extensively used in various applications, including text processing, data manipulation, and web development. Understanding the properties and operations of strings is crucial for any Python programmer.

## [built-in string functions]()