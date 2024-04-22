# **Python Scopes and Namespaces**:
   - A namespace is a mapping of names to objects. In Python, namespaces are implemented as dictionaries.
   - Scopes in Python determine the visibility and lifetime of names (variables) within a program.
   - Python uses the LEGB rule (Local, Enclosing, Global, Built-in) to resolve names in nested scopes.
   - Here's an example demonstrating scopes and namespaces:

```python
x = 10  # Global scope

def foo():
    y = 20  # Enclosing scope

    def bar():
        z = 30  # Local scope
        print(x)  # Access global variable
        print(y)  # Access enclosing variable
        print(z)  # Access local variable

    bar()

foo()
```