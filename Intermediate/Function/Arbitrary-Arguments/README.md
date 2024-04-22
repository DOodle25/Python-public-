### `*args` (Arbitrary Arguments)

## Handling Variable-Length Positional Arguments

- `*args` is used in Python to pass a variable number of positional arguments to a function.
- It allows you to pass a non-keyworded variable-length argument list to the function.

- The asterisk (*) before `args` allows the function to accept any number of positional arguments and stores them as a tuple.
- Inside the function, you can iterate over this tuple to access each argument individually.

```python
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)
# Output:
# 1
# 2
# 3
```

- In this example, the `my_function` accepts a variable number of arguments using `*args`.
- When called with `my_function(1, 2, 3)`, the arguments `(1, 2, 3)` are passed to the function and stored in the `args` tuple.
- The function then iterates over this tuple and prints each argument.

### `**kwargs` (Arbitrary Keyword Arguments)

- Handling Variable-Length Keyword Arguments

- `**kwargs` is used in Python to pass a variable number of keyword arguments to a function.
- It allows you to pass a keyworded variable-length argument list to the function.

- The double asterisks (**) before `kwargs` allows the function to accept any number of keyword arguments and stores them as a dictionary.
- Inside the function, you can access the values associated with each keyword using dictionary access syntax.

```python
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

my_function(name="Alice", age=30, city="New York")
# Output:
# name : Alice
# age : 30
# city : New York
```

- In this example, the `my_function` accepts a variable number of keyword arguments using `**kwargs`.
- When called with `my_function(name="Alice", age=30, city="New York")`, the keyword arguments are passed to the function and stored in the `kwargs` dictionary.
- Inside the function, we iterate over this dictionary and print each key-value pair.

Using `*args` and `**kwargs` allows you to write flexible functions that can accept various combinations of arguments, making your code more versatile and adaptable to different use cases.

