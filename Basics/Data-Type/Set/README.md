# Set[collection of homogeneous/heterogeneous data][mutable]

A set is an unordered collection of unique elements. Sets are defined by enclosing comma-separated elements within curly braces `{}`.

Here are some key characteristics of Python sets:

1. **Unordered**: Sets are unordered, meaning the order of elements is not guaranteed and may change between iterations.

2. **Unique Elements**: Sets contain only unique elements. Duplicate elements are automatically removed.

3. **Mutable**: Sets are mutable, meaning you can add or remove elements after creation.

Now, let's discuss some common operations and methods associated with Python sets:

1. **add(item)**: Adds a single element to the set.

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
```

2. **update(iterable)**: Adds elements from the iterable to the set.

```python
my_set = {1, 2, 3}
my_set.update([4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}
```

3. **remove(item)**: Removes the specified item from the set. Raises a `KeyError` if the item is not found.

```python
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}
```

4. **discard(item)**: Removes the specified item from the set if it is present. Does not raise an error if the item is not found.

```python
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}
```

5. **pop()**: Removes and returns an arbitrary element from the set. Raises a `KeyError` if the set is empty.

```python
my_set = {1, 2, 3}
item = my_set.pop()
print(item)    # Output: 1, 2, or 3
print(my_set)  # Output: {2, 3} or {1, 3} or {1, 2}
```

6. **clear()**: Removes all elements from the set, leaving it empty.

```python
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()
```

7. **copy()**: Returns a shallow copy of the set.

```python
my_set = {1, 2, 3}
copy_set = my_set.copy()
print(copy_set)  # Output: {1, 2, 3}
```

8. **union(other_set)**: Returns a new set containing all elements from both sets (combining sets using `|` operator also achieves the same).

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
```

9. **intersection(other_set)**: Returns a new set containing only the elements that are common to both sets (intersection of sets using `&` operator also achieves the same).

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}
```

10. **difference(other_set)**: Returns a new set containing elements that are present in the first set but not in the second set (difference of sets using `-` operator also achieves the same).

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}
```

11. **symmetric_difference(other_set)**: Returns a new set containing elements that are present in either set, but not in both sets (symmetric difference of sets using `^` operator also achieves the same).

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
```

12. **issubset(other_set)**: Returns `True` if all elements of the set are present in the other set.

```python
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))  # Output: True
```

13. **issuperset(other_set)**: Returns `True` if all elements of the other set are present in the set.

```python
set1 = {1, 2, 3, 4}
set2 = {1, 2}
print(set1.issuperset(set2))  # Output: True
```

14. **isdisjoint(other_set)**: Returns `True` if the set has no elements in common with the other set.

```python
set1 = {1, 2}
set2 = {3, 4}
print(set1.isdisjoint(set2))  # Output: True
```

Sets are commonly used for mathematical operations, removing duplicates from collections, and testing membership or existence. 