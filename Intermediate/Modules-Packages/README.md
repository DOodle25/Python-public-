# Modules and Packages

**1. Modules**:
A module in Python is a file containing Python definitions and statements. The file name is the module name with the suffix `.py`. Modules allow you to logically organize your Python code into reusable units.

**2. Different Ways to Import Modules and Functions**:

- **Importing Entire Module**:
```python
import module_name
```

- **Importing Specific Function or Variable from Module**:
```python
from module_name import function_name
```

- **Importing All Functions and Variables from Module**:
```python
from module_name import *
```

- **Importing Module with Alias**:
```python
import module_name as alias_name
```

- **Importing Specific Function or Variable from Module with Alias**:
```python
from module_name import function_name as alias_name
```

**1. Executing Modules as Scripts**:
You can execute a Python module as a script by adding the following code at the bottom of the module:
```python
if __name__ == "__main__":
    # Code to be executed when the module is run as a script
```

**2. The Module Search Path**:
When you import a module, Python searches for it in the following locations:
   - The directory containing the script (or the current directory if interactive).
   - The directories listed in the PYTHONPATH environment variable.
   - The installation-dependent default path.



**“Compiled” Python Files**:
- Python compiles source files into Python bytecode (.pyc files) automatically to speed up execution. These compiled files are platform-independent and are automatically generated when a module is imported.

**Standard Modules**:
- Python comes with a standard library that contains a vast collection of modules and packages. These modules provide functionalities for various tasks, such as file I/O, networking, math operations, etc.
- Standard modules in Python are pre-built modules that come with the Python installation. These modules provide various functionalities for performing tasks such as file I/O, networking, mathematical operations, working with dates and times, and much more. They are part of the Python Standard Library, which is a collection of modules and packages that extend the capabilities of Python.


1. **`os` Module**:
   - The `os` module provides functions for interacting with the operating system, such as file operations, directory operations, and process management.
   - Example:

```python
import os

# Get the current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# List files and directories in the current directory
files = os.listdir()
print("Files and Directories:", files)

# Create a new directory
os.mkdir("test_directory")

# Rename a file or directory
os.rename("old_name.txt", "new_name.txt")

# Remove a file
os.remove("file_to_remove.txt")

# Remove an empty directory
os.rmdir("empty_directory")
```

2. **`datetime` Module**:
   - The `datetime` module provides classes for working with dates and times.
   - Example:

```python
import datetime

# Get the current date and time
now = datetime.datetime.now()
print("Current Date and Time:", now)

# Get today's date
today = datetime.date.today()
print("Today's Date:", today)

# Create a specific date
birthday = datetime.date(1990, 5, 15)
print("Birthday:", birthday)

# Calculate the difference between two dates
age = today - birthday
print("Age:", age.days // 365)
```

3. **`random` Module**:
   - The `random` module provides functions for generating random numbers, selecting random elements from lists, and shuffling sequences.
   - Example:

```python
import random

# Generate a random integer between 1 and 100
random_number = random.randint(1, 100)
print("Random Number:", random_number)

# Select a random element from a list
fruits = ['apple', 'banana', 'orange', 'grape']
random_fruit = random.choice(fruits)
print("Random Fruit:", random_fruit)

# Shuffle a list
random.shuffle(fruits)
print("Shuffled Fruits:", fruits)
```

4. **`math` Module**:
   - The `math` module provides mathematical functions and constants.
   - Example:

```python
import math

# Calculate the square root of a number
sqrt_value = math.sqrt(16)
print("Square Root:", sqrt_value)

# Calculate the factorial of a number
factorial_value = math.factorial(5)
print("Factorial:", factorial_value)

# Calculate the sine of an angle
angle_in_radians = math.radians(90)
sin_value = math.sin(angle_in_radians)
print("Sine:", sin_value)
```


- **dir()**:
The `dir()` function is used to list the names of attributes in a module or object. It returns a sorted list of strings.

# **Packages**:
Packages are a way of organizing modules into a hierarchical directory structure. A package is a directory containing an `__init__.py` file and one or more modules.

- **Importing * From a Package**:
```python
from package_name import *
```
This imports all modules and sub-packages within the package.

**1. Intra-package References**:
Modules within a package can reference other modules within the same package using relative import syntax.

**2. Packages in Multiple Directories**:
Packages can be spread across multiple directories by adding the directories containing the package directories to the PYTHONPATH environment variable.

```
my_package/
│   __init__.py
│
├── sub_package1/
│   ├── __init__.py
│   └── module1.py
│
└── sub_package2/
    ├── __init__.py
    └── module2.py
```

We can import modules and packages as follows:

```python
# Importing entire module
import my_package.sub_package1.module1

# Importing specific function from module
from my_package.sub_package2.module2 import some_function

# Importing entire package with alias
import my_package.sub_package1 as sp1

# Importing all functions and variables from module
from my_package.sub_package2.module2 import *

# Executing module as script
if __name__ == "__main__":
    print("This module is executed as a script.")

# Intra-package reference
from . import module1
```

This covers the basics of modules, packages, and various ways of importing them in Python. Understanding these concepts is crucial for structuring and organizing your Python projects effectively.