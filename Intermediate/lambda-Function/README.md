# Lambda Function

A lambda function in Python is a small, anonymous function defined using the `lambda` keyword. Lambda functions can have any number of arguments but can only have one expression. They are particularly useful for writing short, concise functions without the need for a formal function definition.

The syntax for a lambda function is:

```python
lambda arguments: expression
```

Here's a breakdown of each part:

- **lambda**: The keyword used to define a lambda function.
- **arguments**: The input parameters or arguments passed to the function. They are separated by commas if there are multiple arguments.
- **expression**: The single expression or calculation that the function performs. The result of this expression is implicitly returned.

Lambda functions are often used as inline functions, passed as arguments to higher-order functions (functions that take other functions as arguments), or used in situations where a full function definition is not necessary or desirable.

Let's see some examples to understand lambda functions better:

1. **Addition of two numbers**:

```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

2. **Multiplication of two numbers**:

```python
multiply = lambda x, y: x * y
print(multiply(2, 3))  # Output: 6
```

3. **Square of a number**:

```python
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

4. **Sorting a list of tuples based on the second element**:

```python
pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
pairs.sort(key=lambda x: x[1])
print(pairs)  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]
```

In this example, the lambda function `lambda x: x[1]` is used as the sorting key, which specifies that the list should be sorted based on the second element of each tuple.
