# File Handling

**1. File Handling**:
File handling in Python allows you to interact with files on your computer's filesystem. It involves tasks such as reading from files, writing to files, and manipulating file contents.

**2. Reading and Writing Files**:
To open a file in Python, you use the `open()` function, which returns a file object. You specify the file path and the mode (read, write, append, etc.) as arguments to the `open()` function.

- **Reading Files**:
```python
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)
```

- **Writing to Files**:
```python
with open('file.txt', 'w') as file:
    file.write('Hello, world!')
```

**3. Methods of File Objects**:
File objects in Python provide various methods for interacting with files. Some common methods include:

- **read()**: Reads the entire contents of the file.
- **readline()**: Reads a single line from the file.
- **readlines()**: Reads all lines from the file and returns them as a list.
- **write()**: Writes the specified string to the file.
- **close()**: Closes the file.
- **seek(offset)**: Moves the file pointer to the specified byte offset.
- **tell()**: Returns the current file pointer position.

**4. Saving Structured Data with JSON**:
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. Python provides a built-in module called `json` for encoding and decoding JSON data.

- **Writing JSON to a File**:
```python
import json

data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)
```

- **Reading JSON from a File**:
```python
import json

with open('data.json', 'r') as json_file:
    data = json.load(json_file)
    print(data)
```

These examples demonstrate how to write structured data (in the form of Python dictionaries) to a JSON file using `json.dump()`, and how to read JSON data from a file using `json.load()`.