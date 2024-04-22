# Regular Expression

Regular expressions (regex) in Python are powerful tools for searching, matching, and manipulating text based on patterns. They provide a concise and flexible means for pattern matching within strings. Python's `re` module provides support for regular expressions. Let's dive into the rules and concepts of regular expressions in Python with examples:

**1. Metacharacters**:
Metacharacters are special characters that represent patterns. Here are some commonly used metacharacters:

- `.`: Matches any single character except newline.
- `^`: Matches the start of the string.
- `$`: Matches the end of the string.
- `*`: Matches zero or more occurrences of the preceding pattern.
- `+`: Matches one or more occurrences of the preceding pattern.
- `?`: Matches zero or one occurrence of the preceding pattern.
- `[]`: Matches any single character within the brackets.
- `|`: Matches either the pattern on its left or the pattern on its right.
- `()`: Groups patterns together.

**2. Quantifiers**:
Quantifiers specify the number of occurrences of a character or a pattern.

- `*`: Matches zero or more occurrences of the preceding pattern.
- `+`: Matches one or more occurrences of the preceding pattern.
- `?`: Matches zero or one occurrence of the preceding pattern.
- `{m}`: Matches exactly `m` occurrences of the preceding pattern.
- `{m,}`: Matches `m` or more occurrences of the preceding pattern.
- `{m,n}`: Matches between `m` and `n` occurrences of the preceding pattern.

**3. Character Classes**:
Character classes match specific sets of characters.

- `\d`: Matches any digit (equivalent to `[0-9]`).
- `\D`: Matches any non-digit character (equivalent to `[^0-9]`).
- `\w`: Matches any alphanumeric character (equivalent to `[a-zA-Z0-9_]`).
- `\W`: Matches any non-alphanumeric character (equivalent to `[^a-zA-Z0-9_]`).
- `\s`: Matches any whitespace character (equivalent to `[\t\n\r\f\v]`).
- `\S`: Matches any non-whitespace character (equivalent to `[^\t\n\r\f\v]`).

**4. Anchors**:
Anchors are used to specify the position of a pattern in a string.

- `^`: Matches the start of the string.
- `$`: Matches the end of the string.
- `\b`: Matches a word boundary (the position between a word character and a non-word character).
- `\B`: Matches a non-word boundary.

**5. Examples**:

```python
import re

# Example 1: Matching a simple pattern
pattern = r'hello'
text = 'hello world'
match = re.search(pattern, text)
print(match.group())  # Output: hello

# Example 2: Using quantifiers
pattern = r'\d+'  # Matches one or more digits
text = 'I have 10 apples and 20 oranges'
matches = re.findall(pattern, text)
print(matches)  # Output: ['10', '20']

# Example 3: Using character classes
pattern = r'\b[A-Z][a-z]+\b'  # Matches capitalized words
text = 'Hello World! This is Python.'
matches = re.findall(pattern, text)
print(matches)  # Output: ['Hello', 'World', 'This', 'Python']

# Example 4: Using anchors
pattern = r'\b\w{3}\b'  # Matches three-letter words
text = 'I have a cat and a dog'
matches = re.findall(pattern, text)
print(matches)  # Output: ['cat', 'and', 'dog']
```
