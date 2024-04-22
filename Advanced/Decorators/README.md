# Decorator

Python decorators are a powerful and flexible tool used to modify or extend the behavior of functions or methods without changing their source code. Decorators allow you to wrap a function with another function to add additional functionality. They are heavily used in Python frameworks like Flask and Django for tasks such as authentication, logging, caching, and more.

Here's how decorators work:

- A decorator is a function that takes another function as an argument and returns a new function.
- The new function usually performs some actions before and/or after calling the original function.
- Decorators are prefixed with the `@` symbol followed by the decorator function name.

Let's explore various use cases of decorators with examples:

**1. Logging**:
A decorator can be used to log information about function calls.

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

result = add(2, 3)  # Output: Calling function add with args: (2, 3), kwargs: {}
print(result)       # Output: 5
```

**2. Authentication**:
A decorator can be used to authenticate access to a function.

```python
def authenticate(func):
    def wrapper(*args, **kwargs):
        if is_authenticated():
            return func(*args, **kwargs)
        else:
            raise PermissionError("Authentication required")
    return wrapper

@authenticate
def restricted_function():
    return "You have access to this restricted function"

restricted_function()  # Output: PermissionError: Authentication required
```

**3. Timing**:
A decorator can be used to measure the execution time of a function.

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def long_running_function():
    time.sleep(2)

long_running_function()  # Output: Execution time of long_running_function: 2.000290870666504 seconds
```

**4. Caching**:
A decorator can be used to cache the results of a function to improve performance.

```python
def cache(func):
    cached_results = {}
    def wrapper(*args):
        if args not in cached_results:
            cached_results[args] = func(*args)
        return cached_results[args]
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))  # Output: 5
```

**5. Validation**:
A decorator can be used to validate function arguments.

```python
def validate(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Arguments must be integers")
        return func(*args, **kwargs)
    return wrapper

@validate
def sum_values(*args):
    return sum(args)

print(sum_values(1, 2, 3))   # Output: 6
print(sum_values(1, 'a', 3))  # Output: TypeError: Arguments must be integers
```

Python provides several predefined decorators that are commonly used in various scenarios. These decorators are available in Python's standard library and can be imported and used in your code. Let's explore some of these predefined decorators along with examples:

**1. `@staticmethod`**:
   - This decorator is used to define static methods within a class.
   - Static methods don't require access to instance attributes and can be called on the class itself.

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

# Static methods can be called on the class itself
print(MathOperations.add(2, 3))  # Output: 5
```

**2. `@classmethod`**:
   - This decorator is used to define class methods within a class.
   - Class methods take the class itself as the first argument (`cls`) and can be called on both the class and instances of the class.

```python
class MathOperations:
    @classmethod
    def multiply(cls, x, y):
        return x * y

# Class methods can be called on the class itself
print(MathOperations.multiply(2, 3))  # Output: 6

# Class methods can also be called on instances of the class
math_obj = MathOperations()
print(math_obj.multiply(2, 3))        # Output: 6
```

**3. `@property`**:
   - This decorator is used to define properties (getter methods) within a class.
   - Properties allow you to access attributes of an object in a more controlled manner.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

# Accessing the property without using parentheses
circle = Circle(5)
print(circle.diameter)  # Output: 10
```

**4. `@classmethod` with `@property`**:
   - You can combine `@classmethod` and `@property` decorators to create class methods that act as properties.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def diameter(self):
        return 2 * self.radius

# Using the class method as a property
circle = Circle.from_diameter(10)
print(circle.diameter)  # Output: 10
```

**5. `@staticmethod` with `@property`**:
   - You can also combine `@staticmethod` and `@property` decorators to create static methods that act as properties.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def pi():
        return 3.14

    @property
    def circumference(self):
        return 2 * self.radius * Circle.pi()

# Using the static method as a property
circle = Circle(5)
print(circle.circumference)  # Output: 31.400000000000002
```
