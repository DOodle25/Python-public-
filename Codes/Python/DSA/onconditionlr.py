class Node:
    data = 0
    left = None
    right = None
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BSTree:
    root = None
    count = 0
    #next_new = Nones

    def manualaddition(self):
        input_ = input().split()
        for i in range(len(input_)):
            _ = input()
            #print(input_[i])
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
            if self.root == None:
                self.root = Node(input_[i])
                #next_new = root.left
                self.count += 1
            else:
                temp = self.root
                while True:
                    if input_[i] == temp.data:
                        break
                    elif _ == "R":
                        if temp.left == None:
                            temp.left = Node(input_[i])
                            self.count += 1
                            break
                        else:
                            temp = temp.left
                            _ = input()
                    elif _ == "L":
                        if temp.right == None:
                            temp.right = Node(input_[i])
                            self.count += 1
                            break
                        else:
                            temp = temp.right
                            _ = input()
    def Inorder(self, node=None):
        if node is None:
            node = self.root
        if node is not None:
            if node.left is not None:
                self.Inorder(node=node.left)
            print(node.data, end = " ")
            if node.right is not None:
                self.Inorder(node=node.right)
    def preorder(self, node=None):
        if node is None:
            node = self.root
        if node is not None:
            print(node.data, end = " ")
            if node.left is not None:
                self.preorder(node=node.left)
            if node.right is not None:
                self.preorder(node=node.right)
    def postorder(self, node=None):
        if node is None:
            node = self.root
        if node is not None:
            if node.left is not None:
                self.postorder(node=node.left)
            if node.right is not None:
                self.postorder(node=node.right)
            print(node.data, end = " ")
    def print_(self):
        print()
        s = self.root
        print(s.data)
        l1 = s.left
        #l2 = s.right
        print(l1.data)
        #l3 = l1.left
        l4 = l1.right
        #l5 = l2.left
        #l6 = l2.right
        print(l4.data)
B = BSTree()    
B.manualaddition()
#B.Inorder()
print()
B.preorder()
print()
B.postorder()
B.print_()