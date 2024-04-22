class Queue:
    def __init__obj(self):
        #initiates queue and implements start and rear element -1
        self.queue = ["\0"] * (int(input("Enter the size of the Queue : ")))
        self.start = 0
        self.rear = -1
        self.command()
    def is_full(self):
        #checks if queue is full
        if self.rear == len(self.queue) - 1:
            return True
        return False
    def is_empty(self):
        #checks if rear is empty
        if self.rear == -1:
            return True
        return False
    def overwrite(self, size_):
        # creates queue for a given size
        self.queue = [0] * int(size_)
        self.start = 0
        self.rear = -1
        print(self.queue)
    def add(self, element_):
        #adds element in queue
        if not self.is_full():
            self.rear += 1
            self.queue[self.rear] = int(element_)
        else:
            print("Queue is filled first pop some element or copy create a bigger queue")
    def remove(self, number_):
        #pops element from queue
        if not self.is_empty():
            for i in range(0, self.rear - int(number_) + 2):
                    self.queue[i] = self.queue[i + int(number_)]
                    self.start += 1
            for j in range(self.start + 1 , self.start + int(number_) + 2):
                self.queue[j] = "\0"
            self.start = 0
            self.rear -= int(number_)
            if self.rear < -1:
                self.rear = -1  
        else:
            print("Queue is empty add something before removing anything")
    def display(self):
        #prints Queue
        if self.rear == -1:
            print("Queue is empty")
        print(self.queue[0:self.rear + 1])
    def command(self):
        # loop to perform operations on stack including making creating and overwriting stack till user wants
        #while(True):
            #ans = input("perform operation of make new object(O/o):")
            #if(ans == "O"):
                command = input("Type(overwrite size)(add element)(pop times)(display) :").split(' ')
                match command[0]:
                    case "overwrite":
                        self.overwrite(command[1])
                        self.command()
                    case "add":
                        self.add(command[1])
                        self.command()
                    case "remove":
                        self.remove(command[1])
                        self.command()
                    case "display":
                        self.display()
                        self.command()
class generator:
    def create_with_name(self):
        l = list()    
stack_obj = Queue()