class Stack:
    def __init__(self):
        #initiates stack and implements top element -1
        self.stack = [0] * (int(input("Enter the size of the stack : ")))
        self.top = -1
        self.command()
    def is_full(self):
        #checks if stack is full
        if self.top == len(self.stack) - 1:
            return True
        return False
    def is_empty(self):
        #checks if stack is empty
        if self.top == -1:
            return True
        return False
    def overwrite(self, size_):
        # creates stack for a given size
        self.stack = [0] * int(size_)
        self.top = -1
        print(self.stack)
    def push(self, element_):
        #adds element in stack
        if not self.is_full():
            self.top += 1
            self.stack[self.top] = int(element_)
        else:
            print("Stack is filled first pop some element or copy create a bigger stack")
    def pop(self, number_):
        #pops element from stack
            for k in range(int(number_)):
                if not self.is_empty():
                    self.stack[self.top] = int(0)
                    self.top -= 1
                else:
                    break
    def peek(self):
        #prints value of top
        if self.top == -1:
            print("Stack is empty")
        print(f"top : {self.stack[self.top]}")
    def display(self):
        #prints stack
        if self.top == -1:
            print("Stack is empty")
        print(self.stack[0:self.top + 1])
    def command(self):
        # loop to perform operations on stack including making creating and overwriting stack till user wants
        #while(True):
            #ans = input("Do you want to perform any operation on the stack(Y/N):")
            #if(ans == "Y" or ans == "y"):
                command = input("Type(overwrite size)(push element)(pop times)(peek)(display) :").split(' ')
                match command[0]:
                    case "overwrite":
                        self.overwrite(command[1])
                        self.command()
                    case "push":
                        self.push(command[1])
                        self.command()
                    case "pop":
                        self.pop(command[1])
                        self.command()
                    case "peek":
                        self.peek()
                        self.command()
                    case "display":
                        self.display()
                        self.command()
stack_obj = Stack()
stack_obj_2 = Stack()