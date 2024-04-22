# dunder

Functions that start and end with double underscores (`__`) in Python are called dunder (short for double underscore) methods or special methods. These methods have special meanings in Python and are used to define behavior for built-in operations. They provide a way to customize the behavior of objects and classes in Python.

1. **`__init__(self, ...)`:**
   - This method is called when an object is initialized (i.e., created).
   - It is commonly used to perform initialization tasks for the object.
   
   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age

   person = Person("Alice", 30)
   ```

2. **`__repr__(self)`:**
   - This method returns a string representation of the object. It is used for debugging and logging purposes.
   
   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age

       def __repr__(self):
           return f"Person(name='{self.name}', age={self.age})"

   person = Person("Alice", 30)
   print(person)  # Output: Person(name='Alice', age=30)
   ```

3. **`__str__(self)`:**
   - This method returns a string representation of the object. It is used for displaying the object to end-users.
   
   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age

       def __str__(self):
           return f"Name: {self.name}, Age: {self.age}"

   person = Person("Alice", 30)
   print(person)  # Output: Name: Alice, Age: 30
   ```

4. **`__len__(self)`:**
   - This method returns the length of the object. It is commonly used for sequences like lists, tuples, and strings.
   
   ```python
   class MyList:
       def __init__(self, items):
           self.items = items

       def __len__(self):
           return len(self.items)

   my_list = MyList([1, 2, 3, 4, 5])
   print(len(my_list))  # Output: 5
   ```

5. **`__getitem__(self, key)`:**
   - This method allows objects to support indexing (e.g., accessing elements using `[]`).
   
   ```python
   class MyList:
       def __init__(self, items):
           self.items = items

       def __getitem__(self, index):
           return self.items[index]

   my_list = MyList([1, 2, 3, 4, 5])
   print(my_list[2])  # Output: 3
   ```

6. **`__setitem__(self, key, value)`:**
   - This method allows objects to support item assignment (e.g., setting values using `[]`).
   
   ```python
   class MyDict:
       def __init__(self):
           self.data = {}

       def __setitem__(self, key, value):
           self.data[key] = value

   my_dict = MyDict()
   my_dict['name'] = 'Alice'
   print(my_dict.data)  # Output: {'name': 'Alice'}
   ```

7. **`__delitem__(self, key)`:**
   - This method allows objects to support item deletion (e.g., using the `del` statement).
   
   ```python
   class MyDict:
       def __init__(self):
           self.data = {}

       def __delitem__(self, key):
           del self.data[key]

   my_dict = MyDict()
   my_dict['name'] = 'Alice'
   del my_dict['name']
   print(my_dict.data)  # Output: {}
   ```
