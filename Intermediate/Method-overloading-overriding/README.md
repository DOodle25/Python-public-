# Method Overriding and Method Overloading

**1. Method Overriding**:

Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The subclass method must have the same name, parameters, and return type as the method in the superclass. When an overridden method is called through an instance of the subclass, the subclass's implementation of the method is executed instead of the superclass's implementation.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Overrides the speak method of the Animal class
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Dog barks
```

In the example above, the `speak` method in the `Dog` class overrides the `speak` method in the `Animal` class. When `dog.speak()` is called, it executes the `speak` method defined in the `Dog` class, not the one in the `Animal` class.

**2. Method Overloading**:

Python does not support method overloading in the same way as some other programming languages like Java or C++. In those languages, method overloading allows multiple methods with the same name but different parameter lists to coexist in the same class.

However there are ways to achieve it
