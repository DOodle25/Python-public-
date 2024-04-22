class Data:
    a = 20
    def fun():
        a = 10
        name = input("Enter your name: ")
        print(f"Hello, {name}")
    def fun2():
        print("Hello, World!")

obj1 = Data()
obj1.fun()
Data.fun()
print(id(Data))
print(id(obj1))
print(Data.a)