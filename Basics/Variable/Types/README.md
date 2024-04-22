# Variable Types[According to scope]

In Python, variables can have different scopes, which define where in the code the variable is accessible and how long it persists in memory. The scope of a variable determines its visibility and lifetime. Python supports four main variable scopes:

1. **Local Variables**:
   - Local variables are defined within a function or a block of code and are accessible only within that function or block.
   - They are created when the function or block is entered and destroyed when it exits.
   - Local variables cannot be accessed from outside the function or block where they are defined.
   
Example of local variables:

```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Output: 10

# Trying to access the local variable outside the function will raise an error
# print(x)  # Error: NameError: name 'x' is not defined
```

2. **Enclosing (Nonlocal) Variables**:
   - Enclosing variables are defined in an enclosing function (a function containing other functions) and are accessible by nested functions.
   - They are accessible within the nested functions but not outside the enclosing function.
   
Example of enclosing variables:

```python
def outer_function():
    x = 10  # Enclosing variable
    def inner_function():
        print(x)
    inner_function()

outer_function()  # Output: 10

# Trying to access the enclosing variable outside the enclosing function will raise an error
# print(x)  # Error: NameError: name 'x' is not defined
```

3. **Global Variables**:
   - Global variables are defined at the top level of a module (outside any function or block) and are accessible throughout the module.
   - They are visible to all functions and blocks within the module.
   
Example of global variables:

```python
x = 10  # Global variable

def my_function():
    print(x)

my_function()  # Output: 10

# Global variables can be accessed and modified from anywhere in the module
print(x)  # Output: 10
```

4. **Built-in Variables**:
   - Built-in variables are predefined in Python and are accessible from any part of the code.
   - They are part of the Python language itself and include objects like `True`, `False`, `None`, and functions like `print()`, `len()`, etc.
   
Example of built-in variables:

```python
print(True)   # Output: True
print(len([1, 2, 3]))  # Output: 3
```


**Class and Instance Variables**:
   - Class variables are shared among all instances of a class, while instance variables are unique to each instance.
   - Class variables are defined within the class body, outside of any method, and are accessed using the class name or instance.
   - Instance variables are defined within the constructor (`__init__` method) and are accessed using the instance.
   - Here's an example demonstrating class and instance variables:

```python
class MyClass:
    class_variable = "This is a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

# Accessing class variable
print(MyClass.class_variable)   # Output: This is a class variable

# Creating instances and accessing instance variables
obj1 = MyClass("Instance 1")
obj2 = MyClass("Instance 2")
print(obj1.instance_variable)  # Output: Instance 1
print(obj2.instance_variable)  # Output: Instance 2
```
