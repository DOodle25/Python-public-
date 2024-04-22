# Control Statement

1. **If Statement**:
The `if` statement is used to execute a block of code if a specified condition is true.

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

2. **Elif Statement**:
The `elif` (short for "else if") statement allows you to check multiple conditions after the initial `if` statement. It is used when you have more than one condition to evaluate.

```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
```

3. **Else Statement**:
The `else` statement is used to execute a block of code if the preceding `if` or `elif` conditions are not met.

```python
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
```

4. **For Loop**:
The `for` loop is used to iterate over a sequence (such as a list, tuple, string, or dictionary) and execute a block of code for each item in the sequence.

```python
for i in range(5):
    print(i)
```

5. **While Loop**:
The `while` loop is used to repeatedly execute a block of code as long as a specified condition is true.

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

6. **Break Keyword**:
The `break` keyword is used to exit the current loop prematurely, regardless of whether the loop condition has been satisfied or not.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

7. **Continue Keyword**:
The `continue` keyword is used to skip the rest of the code inside a loop for the current iteration and proceed to the next iteration.

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

8. **Pass Keyword**:
The `pass` keyword is used as a placeholder when a statement is syntactically required but you want to do nothing.

```python
x = 10
if x > 5:
    pass
else:
    print("x is less than or equal to 5")
```
