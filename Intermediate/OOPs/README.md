# OOPs

Object-Oriented Programming (OOP) is a programming paradigm that revolves around the concept of objects, which are instances of classes. Python is an object-oriented programming language that supports the following OOP concepts:

**1. Classes and Objects**:
   - A class is a blueprint for creating objects. It defines properties (attributes) and behaviors (methods) that the objects of the class will have.
   - An object is an instance of a class. It represents a real-world entity and encapsulates data and methods that operate on that data.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def drive(self):
        print(f"Driving {self.make} {self.model}")

car1 = Car("Toyota", "Camry")
car1.drive()  # Output: Driving Toyota Camry
```

**2. Inheritance**:
   - Inheritance is a mechanism where a new class inherits properties and behaviors from an existing class.
   - The existing class is called the base class or superclass, and the new class is called the derived class or subclass.
   - The derived class can extend or override the functionalities of the base class.

```python
class ElectricCar(Car):  # ElectricCar inherits from Car
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)  # Call the constructor of the base class
        self.battery_capacity = battery_capacity
    
    def charge(self):
        print(f"Charging {self.make} {self.model}")

electric_car1 = ElectricCar("Tesla", "Model S", 100)
electric_car1.drive()   # Output: Driving Tesla Model S (inherited from Car)
electric_car1.charge()  # Output: Charging Tesla Model S
```

**3. Types of Inheritance in Python**:

- **Single Inheritance**: A derived class inherits from only one base class.
```python
class A:
    pass

class B(A):
    pass
```

- **Multiple Inheritance**: A derived class inherits from multiple base classes.
```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

- **Multilevel Inheritance**: A derived class inherits from another derived class.
```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

- **Hierarchical Inheritance**: Multiple derived classes inherit from a single base class.
```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass
```

- **Hybrid Inheritance**: Combination of any two or more types of inheritance.
```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass
```

**4. Method Overriding**:
   - Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Dog barks
```

**5. Encapsulation**:
   - Encapsulation is the bundling of data and methods that operate on that data within a single unit or class.
   - It hides the internal state of an object and only exposes necessary functionalities.

```python
class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

account = BankAccount()
account.deposit(100)
account.withdraw(50)
print(account.balance)  # Output: 50
```