class node(Object):

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNExt(self):
        return self.next

class LinkedList(object):

    def __init__(self):
        self.head = None

    def printLinkedList(Self):
        temp = self.head
        while(temp.next):
            print(temp.data, end='->')
            temp = temp.next
        
        print(temp.data)

    
