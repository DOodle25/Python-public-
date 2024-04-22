class Node:
    data = 0
    next = None
    prev = 0
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = "Start"
class List:
    root = None

    def append(self, data):
        t = Node(data)
        if not self.root:
            self.root = t
            return
        x = self.root
        while x.next:
            x = x.next
        t.prev = x
        x.next = t

    def List_(self):
        str_ = input().split()
        for i in str_:
            self.append(int(i))

    def __len__(self):
        l = 0
        x = self.root
        while x:
            l += 1
            x = x.next
        return l

    def __repr__(self):
        if not self.root:
            return "[ ]"
        result = "["
        x = self.root
        while x.next:
            result += str(x.data) + ", "
            x = x.next
        result += str(x.data) + "]"
        return result

    def display(self):
        x = self.root
        while x.next:
            print(x.data, end="-->")
            x = x.next
        print(x.data)
        print()
        while not x.prev == "Start":
            print(x.data, end = "")
            print("-->" ,end = "")
            x = x.prev
        print(x.data)
        print()

    def count(self, data):
        pass

    def index(self, data):
        if not self.root:
            return -1
        x = self.root
        c = 0
        while x:
            if x.data == data:
                return c
            c += 1
            x = x.next
        return -1

    def start_add(self, data):
        x = Node(data)
        x.next = self.root
        self.root = x

my_list = List()
my_list.List_()
my_list.display()
my_list.start_add(99)
my_list.display()