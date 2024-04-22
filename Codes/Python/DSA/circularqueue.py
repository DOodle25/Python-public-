class CircularQueue:
    def __init__(self):
        #initiates queue and implements start and rear element -1
        self.queue = ["\0"] * (int(input("Enter the size of the Queue : ")))
        self.start = 0
        self.rear = -1
        self.command()
    def is_full(self):
        #checks if queue is full
        if (self.start == 0 and self.rear == len(self.queue) - 1) or (self.start == len(self.queue) - 1 and self.rear == 0) or ((self.start == ((self.rear + 1) % len(self.queue))) and not(self.rear == -1 and self.start == 0)):
            return True
        return False
    def is_empty(self):
        #checks if rear is empty but his one is only for remove
        if self.start == self.rear:
            self.queue[self.start] = "\0"
            self.start, self.rear = 0, -1
            return True
        return False
    def overwrite(self, size_):
        # creates queue for a given size
        self.queue = [0] * int(size_)
        self.start = 0
        self.rear = 0
        print(self.queue)
    def insert(self, element_):
        #adds element in queue
        if not self.is_full():
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = int(element_)
        else:
            print("Queue is filled first pop some element or copy create a bigger queue")
    def remove(self, number_):
        for i in range(0, int(number_)):
            if not self.is_empty():
                self.queue[self.start] = "\0"
                self.start = (self.start + 1) % len(self.queue)
            else:
                print("Queue is empty add something before removing anything")
                break
    def display(self):
        print(self.queue)
        if self.start == self.rear + 1:
            print("Queue is empty")
        else:
            s = self.start
            r = self.rear
            while True:
                if s == r:
                    print(self.queue[s])
                    break
                else:
                    print(self.queue[s], end = " ")
                    s = (s + 1) % len(self.queue)
        print(f"s:{self.start} r:{self.rear}")
    def command(self):
        # loop to perform operations on stack including making creating and overwriting stack till user wants
        #while(True):
            #ans = input("perform operation of make new object(O/o):")
            #if(ans == "O"):
                command = input("Type(overwrite size)(insert element)(remove times)(display) :").split(' ')
                match command[0]:
                    case "overwrite":
                        self.overwrite(command[1])
                        self.command()
                    case "insert":
                        self.insert(command[1])
                        self.command()
                    case "remove":
                        self.remove(command[1])
                        self.command()
                    case "display":
                        self.display()
                        self.command()
#class generator:
    #def create_with_name(self):
        #l = list()    
queue_obj = CircularQueue()