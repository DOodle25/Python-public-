# Variable

In Python, a variable is a named reference to a value stored in memory. Variables play a crucial role in programming as they allow developers to store and manipulate data dynamically. When you create a variable, you're essentially allocating space in the computer's memory to store a value, and you can refer to that value by its name throughout your program.

Here are some key points to understand about variables in Python:

1. **Dynamic Typing**: Python is dynamically typed, meaning you don't need to explicitly declare the data type of a variable when you create it. The data type of a variable is inferred based on the value assigned to it.

   ```python
   x = 10       # x is an integer
   y = "hello"  # y is a string
   ```

2. **Variable Naming Rules**:
   - Variable names can contain letters, numbers, and underscores.
   - Variable names must start with a letter or an underscore (but it's recommended to start with a letter).
   - Variable names are case-sensitive (`name` and `Name` are different variables).
   - Variable names cannot be a Python keyword or reserved word (e.g., `if`, `for`, `while`, `class`, etc.).[it actually is possible but you won't be able to access that function cause the keyword is now pointing to the new value]

3. **Assignment**: Assigning a value to a variable is done using the `=` operator.

   ```python
   x = 10
   ```

4. **Variable Reassignment**: You can change the value of a variable by assigning a new value to it.

   ```python
   x = 10
   x = 20  # Reassigning the value of x
   ```

5. **Variable Scope**: Variables have a scope, which defines where in the code they can be accessed. Variables defined within a function have local scope and can only be accessed within that function. Variables defined outside of any function have global scope and can be accessed from anywhere in the program.

   ```python
   global_var = 10  # Global variable

   def my_function():
       local_var = 20  # Local variable
       print(global_var)  # Accessing global variable
       print(local_var)   # Accessing local variable

   my_function()
   ```

6. **Deleting Variables**: You can delete a variable using the `del` keyword.

   ```python
   x = 10
   del x
   ```

7. **Immutable vs. Mutable**: In Python, variables can hold both immutable (e.g., integers, strings, tuples) and mutable (e.g., lists, dictionaries) objects. Immutable objects cannot be changed after creation, while mutable objects can be modified.

   ```python
   x = 10  # Immutable
   y = [1, 2, 3]  # Mutable
   ```

Variables are fundamental in Python programming, and understanding how to declare, assign, and use them effectively is essential for writing Python code.