class Node:
    data = 0
    next_ = None
    prev = None
    def __init__(self, data):
        self.data = data

class DoublyLinkedList:
    start = None
    end = None
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
                temp.next_.prev = temp
                self.end = temp.next_
            else:
                new_add = Node(input_[i])
                self.start = new_add
                new_add.prev = None
                self.end = new_add
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
            temp.next_ = Node(input_[i])
            temp.next_.prev = temp
            self.end = temp.next_
        else:
            new_add = Node(input_[i])
            self.start = new_add
            new_add.prev = None
            self.end = new_add
        
    def display(self):
        temp = self.start
        while temp.next_:
            print(temp.data, end = "-->")
            temp = temp.next_
        print((temp.data))
    def displayBack(self):
        temp = self.end
        while temp.prev:
            print(temp.data, end = "-->")
            temp = temp.prev
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
        if index == -1 or index > self.len():
            temp = self.start
            while temp:
                if temp.next_.next_ == None:
                    #del temp.next_
                    break
                else:
                    temp = temp.next_
            temp.next_ = None
            self.end = temp
        else:
            count = 1
            temp = self.start
            while True:
                if count == index:
                    #del temp.next_
                    temp.next_ = temp.next_.next_
                    temp.next_.next_.prev = temp
                    break
                else:
                    count += 1
                    temp = temp.next_
    def inert(self):
        pass
    def reverse(self):
        pass
    def sort(self):
        pass
    def __add__(self):
        pass
    def __mul__(self, x, y):
        pass
            

L = DoublyLinkedList()
L.MakeLinkedList()
#L.AddSingle()
#L.AddSingle()
#L.AddSingle()
#L.AddSingle()
#L.AddSingle()
L.display()
print()
L.displayBack()
print()
for i in L:
    print(type(i))
#print(L.len())
#print(L.count(40))
#print(L.index(40))
#x = input()
#y = input()
#z = x + y++
#print(z)
#print(x + y)
L.pop(3)
print()
L.display()
print()
L.displayBack()
print()
print(L)