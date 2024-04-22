def overload(*types):
    def decorator(func):
        if not hasattr(func, 'overloads'):
            func.overloads = []
        func.overloads.append(types)
        return func
    return decorator

def resolve_overload(func, *args, **kwargs):
    for types in func.overloads:
        if len(args) == len(types) and all(isinstance(arg, t) for arg, t in zip(args, types)):
            return func(*args, **kwargs)
    raise TypeError(f"No matching overload found for {func.__name__}")

class Overloaded:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return OverloadedInstance(self.name, instance)

class OverloadedInstance:
    def __init__(self, name, instance):
        self.name = name
        self.instance = instance

    def __call__(self, *args, **kwargs):
        method = getattr(self.instance, self.name)
        return resolve_overload(method, *args, **kwargs)

class MyClass:
    def __init__(self):
        pass

    @overload(int)
    def add(self, x):
        return x + 10

    @overload(str)
    def add(self, s):
        return s + " Hello"

    @property
    def add(self):
        return Overloaded('add')

# Example usage
obj = MyClass()
print(obj.add(5))    # Output: 15
print(obj.add("Hi")) # Output: Hi Hello
  



  