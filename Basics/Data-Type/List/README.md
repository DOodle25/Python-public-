# List[collection of homogeneous/heterogeneous data][mutable]

**In Python, a list is a mutable, ordered collection of elements. Lists can contain elements of different data types, including integers, strings, floats, and even other lists. Lists are defined by enclosing comma-separated elements within square brackets `[ ]`. Here are some key characteristics of Python lists:**

1. **Mutable**: Lists are mutable, meaning you can modify their elements after creation. You can add, remove, or change elements in a list.

2. **Ordered**: Lists maintain the order of elements as they are inserted. The order of elements in a list is preserved unless explicitly modified.

3. **Indexing**: Elements in a list can be accessed using zero-based indices. Negative indices can also be used to access elements from the end of the list.

4. **Dynamic**: Lists in Python can dynamically resize, meaning they can grow or shrink as needed to accommodate new elements or remove existing ones.

## common operations and methods associated with Python lists:

1. **append(item)**: Adds a single element to the end of the list.

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

2. **insert(index, item)**: Inserts an element at the specified index in the list.

```python
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)  # Output: [1, 5, 2, 3]
```

3. **extend(iterable)**: Extends the list by appending elements from the iterable.

```python
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]
```

4. **pop(index)**: Removes and returns the element at the specified index. If no index is provided, it removes and returns the last element.

```python
my_list = [1, 2, 3, 4, 5]
item = my_list.pop(2)
print(item)      # Output: 3
print(my_list)   # Output: [1, 2, 4, 5]
```

5. **remove(item)**: Removes the first occurrence of the specified item from the list.

```python
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)
print(my_list)   # Output: [1, 3, 2, 4]
```

6. **clear()**: Removes all elements from the list, leaving it empty.

```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list)   # Output: []
```

7. **count(item)**: Returns the number of occurrences of the specified item in the list.

```python
my_list = [1, 2, 3, 2, 4]
print(my_list.count(2))   # Output: 2
```

8. **index(item)**: Returns the index of the first occurrence of the specified item in the list.

```python
my_list = [1, 2, 3, 2, 4]
print(my_list.index(2))   # Output: 1
```

9. **reverse()**: Reverses the order of elements in the list.

```python
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)   # Output: [3, 2, 1]
```

10. **sort()**: Sorts the elements of the list in ascending order. For lists containing elements of different data types, the sort method may raise a `TypeError`.

```python
my_list = [3, 1, 2]
my_list.sort()
print(my_list)   # Output: [1, 2, 3]
```

11. **copy()**: Returns a shallow copy of the list. Modifications to the copy will not affect the original list, and vice versa.

```python
my_list = [1, 2, 3]
copy_list = my_list.copy()
copy_list.append(4)
print(my_list)    # Output: [1, 2, 3]
print(copy_list)  # Output: [1, 2, 3, 4]
```

## Copy types

1. **Reference**:
   - In Python, when you assign one variable to another, you are creating a reference to the same object in memory. Any changes made to one variable will affect the other because they both point to the same object.

```python
list1 = [1, 2, 3]
list2 = list1  # list2 is a reference to the same object as list1
list2.append(4)
print(list1)  # Output: [1, 2, 3, 4]
```

2. **Shallow Copy**:
   - A shallow copy creates a new object in memory but inserts references to the original objects found in the source.
   - Changes to the copied object's elements will affect the original object's elements, but changes to the structure of the copied object (like adding or removing elements) won't affect the original object.

```python
import copy

list1 = [[1, 2], [3, 4]]
list2 = copy.copy(list1)  # Shallow copy
list2[0][0] = 5
print(list1)  # Output: [[5, 2], [3, 4]]
```

3. **Deep Copy**:
   - A deep copy creates a completely new object in memory and recursively copies all the elements and sub-elements from the original object.
   - Changes to the copied object won't affect the original object, and vice versa.

```python
import copy

list1 = [[1, 2], [3, 4]]
list2 = copy.deepcopy(list1)  # Deep copy
list2[0][0] = 5
print(list1)  # Output: [[1, 2], [3, 4]]
```

**Usage**:

- Use **references** when you want multiple variables to point to the same object, and changes to one should affect all others.
- Use **shallow copy** when you need to create a new object with the same contents as the original, but you don't want changes to the structure of the new object to affect the original.
- Use **deep copy** when you need to create a completely independent copy of the original object, where changes to one won't affect the other.
