class MyClass:
    def my_method(self, arg1=None, arg2=None):
        if arg1 is not None and arg2 is not None:
            # Behavior for when both arg1 and arg2 are provided
            print("Two arguments provided:", arg1, arg2)
        elif arg1 is not None:
            # Behavior for when only arg1 is provided
            print("One argument provided:", arg1)
        else:
            # Default behavior
            print("No arguments provided")

    def my_method(self, arg1):
        # Behavior for when only arg1 is provided
        print("One argument provided:", arg1)

obj = MyClass()
obj.my_method(10)            # Output: One argument provided: 10
obj.my_method(10, 20)        # Output: Two arguments provided: 10 20
