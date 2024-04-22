# Python-Function

Functions are a fundamental concept in Python programming. They allow you to encapsulate reusable blocks of code, making your programs more organized, modular, and easier to maintain. In this guide, we'll explore how to define and call functions in Python, covering their syntax, parameters, return values, and best practices.
- `def` is used used for defining a new fucntion
- The execution of a function introduces a new symbol table used for the local variables of the function. More precisely,
all variable assignments in a function store the value in the local symbol table; whereas variable references first look
in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and
finally in the table of built-in names.
- The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function
when it is called; thus, arguments are passed using call by value.
A function definition associates the function name with the function object in the current symbol table. The interpreter
recognizes the object pointed to by that name as a user-defined function. Other names can also point to that same
function object and can also be used to access the function.

ex:
- The statement result.append(a) calls a method of the list object result. A method is a function
that ‘belongs’ to an object and is named obj.methodname, where obj is some object (this may be an
expression), and methodname is the name of a method that is defined by the object’s type. Different types
define different methods. Methods of different types may have the same name without causing ambiguity. (It
is possible to define your own object types and methods, using classes, see Classes) The method append()
shown in the example is defined for list objects; it adds a new element at the end of the list. In this example it
is equivalent to result = result + [a], but more efficient.

Calling Functions with parameters
- giving only the mandatory argument: ask_ok('Do you really want to quit?'
- giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)
- or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

1. Defining Functions:
     ```
     def function_name(parameter1, parameter2, ...):
         # Function body
         # Statements
         return value
     ```
   - Example:
     ```python
     def greet(name):
         return f"Hello, {name}!"
     ```
2. Returning Value:
- `return` is used for return value from function
- The return statement returns with a value from a function. return without an expression argument returns None. Falling off the end of a function also returns None.

3. Default Parameters:
     - Functions can have default parameter values, which are used if no argument is provided for that parameter.
     ```python
     def greet(name="World"):
         return f"Hello, {name}!"

     print(greet())       # Output: Hello, World!
     print(greet("Alice"))# Output: Hello, Alice!
     ```

4. Keyword Arguments:
     - You can pass arguments to a function using the parameter names (keywords).This allows you to specify arguments in any order and skip optional arguments.

     ```python
     def greet(name, greeting="Hello"):
         return f"{greeting}, {name}!"

     print(greet("Alice"))                # Output: Hello, Alice!
     print(greet("Bob", greeting="Hi"))   # Output: Hi, Bob!
     ```
