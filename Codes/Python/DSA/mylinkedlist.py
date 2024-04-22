class Node:
    data = 0
    next_ = None
    def __init__(self, data):
        self.data = data

class LinkedList:
    start = None
    def __iter__(self):
        self.nexto = self.start
        return self
    def __next__(self):
        if self.nexto:
            current_data = self.nexto.data
            self.nexto = self.nexto.next_
            return current_data
        else:
            raise StopIteration
    def __repr__(self):
        if not self.start:
            return '[ ]'
        temp = self.start
        print(end='[')
        while temp.next_:
            print(temp.data,end='-->')
            temp = temp.next_
        print(temp.data,end=']')
        return ''
    def len(self):
        temp = self.start
        count = -1
        while temp:
            count += 1
            temp = temp.next_
        return count

    def MakeLinkedList(self):
        input_ = input().split()
        for i in range(len(input_)):
            print(input_[i])
            try:
                input_[i] = int(input_[i])
            except ValueError:
                try:
                    input_[i] = float(input_[i])
                except ValueError:
                    try:
                        input_[i] = eval(input_[i])
                    except (SyntaxError, NameError):
                        input_[i] = str(input_[i])
            print(input_[i])
        #for i in [y for y in input().split()]:  
        #for i in [int(y) for y in input().split()]:
            temp = self.start
            if not self.start == None:
                while temp.next_:
                    temp = temp.next_
                temp.next_ = Node(input_[i])
            else:
                new_add = Node(input_[i])
                self.start = new_add
    def AddSingle(self):
        temp = self.start
        new_data = input()
        try:
            new_data = int(new_data)
        except ValueError:
            try:
                new_data = float(new_data)
            except ValueError:
                try:
                    new_data = eval(new_data)
                except (SyntaxError, NameError):
                    new_data = str(new_data)
        #new_data = int(input())
        if not self.start == None:
                while temp.next_:
                    temp = temp.next_
                temp.next_ = Node(new_data)
        else:
            new_add = Node(new_data)
            self.start = new_add
        
    def display(self):
        temp = self.start
        while temp.next_:
            print(temp.data, end = "-->")
            temp = temp.next_
        print((temp.data))
    
    def count(self, key):
        if not self.start:
            return 0
        temp = self.start
        count = 0
        while temp:
            if temp.data == key:
                count += 1
            temp = temp.next_
        return count
    def index(self,key):
        if not self.start:
            return -1
        temp = self.start
        count = 0
        while temp:
            if temp.data == key:
                return count
            count += 1
            temp = temp.next_
        return -1
    def pop(self, index = -1):
        if not self.start:
            return
        len_ = self.len() - 1
        if index == -1:
            index = self.len()  + 1
        if index < 0:
            index = len_ + index
        if index >= len_:
            index = len_ - 1
        temp_ = 0
        temp = self.start
        if index <= 0:
            temp_ = temp.data
            self.start = temp.next_
            temp.next_ = None
            del temp.data
            del temp.next_
            del temp
            return temp_
        while index - 1:
            temp = temp.next_
            index -= 1
        temp2 = temp.next_
        temp.next_ = temp2.next_
        temp2.next_ = None
        temp_ = temp2.data
        del temp2.data
        del temp2.next_
        del temp2
        return temp_
    def insert(self, index = -1):
        new_data = input("data:")
        try:
            new_data = int(new_data)
        except ValueError:
            try:
                new_data = float(new_data)
            except ValueError:
                try:
                    new_data = eval(new_data)
                except (SyntaxError, NameError):
                    new_data = str(new_data)
        if index == -1 or index >self.len():
            temp = self.start 
            while temp.next_:
                temp = temp.next_
            temp.next_ = Node(new_data)
        else:
            temp = self.start
            count = 0
            while True:
                if count == index:
                    temp_ad = temp.next_.next_
                    temp.next_ = Node(new_data)
                    temp.next_.next_ = temp_ad
                    break
                else:
                    count += 1
                    temp = temp.next_
    def reverse(self):
        pass
    def sort(self):
        pass
    def __add__(self):
        pass
    def __mul__(self, x, y):
        start = None
        s1, s2 = x.start , y.start
        for i in range (min(x.len(), y.len())):
            if start == None:
                start = Node(s1.next_.data * s2.next_.data)
                s1 = s1.next_
                s1 = s2.next_
            else:
                temp = start
                while temp.next_:
                    temp = temp.next_
                temp.next_ = Node(Node(s1.next_.data * s2.next_.data))
                s1 = s1.next_
                s1 = s2.next_
        return print(start)
            

L = LinkedList()
L.MakeLinkedList()
L.display()
#L.AddSingle()
#L.AddSingle()
#L.AddSingle()
#L.AddSingle()
#L.AddSingle()
L.display()
for i in L:
    print(type(i))
L.display()
print(L.len())
print(L.count(40))
print(L.index(40))
#x = input()
#y = input()
#z = x + y
#print(z)
#print(x + y)
L.pop(3)
L.insert(3)
print(L)