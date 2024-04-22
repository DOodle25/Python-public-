# Match - Case

In Python, `match` is a new feature introduced in Python 3.10 as part of Pattern Matching (PEP 634). It provides a way to perform pattern matching against values and execute corresponding code blocks based on the matched pattern. Pattern matching is a powerful tool for writing concise and readable code, especially in scenarios where you need to match values against multiple patterns and execute different actions based on the match.

Here's a basic explanation of how `match` works with examples:

Consider a simple scenario of matching different types of animals and performing specific actions based on the matched animal:

```python
def describe_animal(animal):
    match animal:
        case 'dog':
            print("This is a dog.")
        case 'cat':
            print("This is a cat.")
        case 'bird':
            print("This is a bird.")
        case _:
            print("Unknown animal.")
```

In this example:

- `match` is used to match the `animal` value against different patterns.
- `case 'dog':`, `case 'cat':`, and `case 'bird':` are specific patterns to match against the `animal` value.
- `_` is a wildcard pattern that matches anything. It acts as a default case when no other patterns match.

Let's see how this function works with different inputs:

```python
describe_animal('dog')   # Output: This is a dog.
describe_animal('cat')   # Output: This is a cat.
describe_animal('bird')   # Output: This is a bird.
describe_animal('fish')   # Output: Unknown animal.
```

In the above example, when you call `describe_animal('dog')`, it matches the pattern `case 'dog':` and prints "This is a dog.". Similarly, for other animals.

`match` statements can also be used to destructure complex data structures such as tuples or lists. For example:

```python
def process_point(point):
    match point:
        case (0, 0):
            print("Origin")
        case (x, 0):
            print(f"Point on x-axis: x={x}")
        case (0, y):
            print(f"Point on y-axis: y={y}")
        case (x, y):
            print(f"Arbitrary point: x={x}, y={y}")

process_point((0, 0))     # Output: Origin
process_point((3, 0))     # Output: Point on x-axis: x=3
process_point((0, 5))     # Output: Point on y-axis: y=5
process_point((2, 3))     # Output: Arbitrary point: x=2, y=3
```

In this example, the `match` statement destructures the `point` tuple and matches against various patterns like `(0, 0)`, `(x, 0)`, `(0, y)`, and `(x, y)`.
