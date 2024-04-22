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
    dict_ = dict()
    #print(arr)
    #next_new = None

    def makeBSTree(self):
        input_ = input().split()
        for i in range(len(input_)):
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
                #ele = self.root
                #self.arr.append(ele)
                #next_new = root.left
                self.count += 1
            else:
                temp = self.root
                while True:
                    if input_[i] == temp.data:
                        break
                    elif input_[i] < temp.data:
                        if temp.left == None:
                            temp.left = Node(input_[i])
                            self.count += 1
                            #ele = temp.left
                            #self.arr.append(ele)
                            break
                        else:
                            temp = temp.left
                    else:
                        if temp.right == None:
                            temp.right = Node(input_[i])
                            self.count += 1
                            #ele = temp.right
                            #self.arr.append(ele)
                            break
                        else:
                            temp = temp.right
    #def move_up(self, node, parent_store):
        #if node.left is not None:
            #parent_store = node.left
    #def level_pop(self):

    def right_pop(self):
        temp = self.root
        while True:
            if self.root.left is None and self.root.right is None:
                self.root = None
                break
            elif temp.right is not None and temp.right.left is None and temp.right.right is None:
                #del temp.right
                temp.right = None
                break
            elif temp.left is not None and temp.left.left is None and temp.left.right is None:
                #del temp.left
                temp.left = None
                break
            elif temp.right is None:
                temp = temp.left
            else:
                temp = temp.right
    def delete_(self, data = -1):
        ad , temp = self.search_(data)
        print(ad.data, temp.data)
        #leaf node deletion
        if ad.right is None and ad.left is None:
            #del ad
            #print("leaf delete")
            if temp.right is ad:
                temp.right = None
            else:
                temp.left = None
        elif data is self.root.data:
            #print("node delete")
            if self.root.right is None:
                if self.root.left is not None:
                    self.root = self.root.left
            elif self.root.left is not None:
                if self.root.right is not None:
                    self.root = self.root.right
            elif self.root.right is None and self.root.left is None:
                self.root = None
            else:
                l = self.root.left
                self.root = self.root.right
                temp = self.root
                while True:
                    if temp.left is None:
                        temp.left = l
                        break
                    else:
                        temp = temp.left     
        else:
            #print("middle delete")
            #print(ad.right.data)
            #print(ad.left)
            if ad.right is None:
                if ad.left is not None:
                    #print("!")
                    if temp.right is ad:
                        temp.right = temp.right.left
                    else:
                        temp.left = temp.left.left
            elif ad.left is None:
                if ad.right is not None:
                    #print("*")
                    if temp.right is ad:
                        temp.right = temp.right.right
                    else:
                        temp.left = temp.left.right     
            else:
                #print("^")
                l = ad.left
                #print(f"l data:{l.data}")
                #print(temp.right.data, temp.left.data)
                if temp.left == ad:
                    temp_ = temp.left.right
                    temp.left = temp.left.right  
                else:
                    temp_ = temp.left.right
                    temp.right = temp.left.right
                #print(f"temp_:{temp_.data}")
                while True:
                    #print(temp_.left)
                    if temp_.left is None:
                        temp_.left = l
                        break
                    else:
                        temp_ = temp_.left
    def level_delete(self):
        self.levelorder()
        count = 0
        l = None
        while True:
            flag = 0
            count += 1
            if count in self.dict_:
                flag = 1
                l_ = self.dict_[count]
                l_.reverse()
                l = int(l_[0])
        node = self.root
        while True:
            if self.root.data == l:
                self.root = None
                break
            if (node.left and node.left.data == l) or (node.right and node.data.right == l):
                if (node.left and node.data.left == l):
                    node.left.data = None
                    break
                elif (node.right and node.data.right == l):
                    node.right.data = None
                    break
            elif l > node.data:
                node = node.right
            else:
                node = node.left
 
    def search_(self, data, temp = None):
        #generic search
        if temp is None:
            temp = self.root
        if data == self.root.data:
            return self.root, temp
        elif temp.left and temp.left.data == data:
            ad = temp.left
            print(temp.left.data)
            return ad, temp
        elif temp.right and temp.right.data == data:
            ad = temp.right
            print(temp.right.data)
            return ad, temp
        elif temp.right is None and temp.left is None:
            return
        elif temp.right is None:
            return self.search_(data, temp.left)
        else:
            return self.search_(data, temp.left)
            return self.search_(data, temp.right)
    def Inorder(self, node=None):
        if node is None:
            node = self.root
        if node is not None:
            if node.left is not None:
                self.Inorder(node = node.left)
            print(node.data, end = " ")
            if node.right is not None:
                self.Inorder(node = node.right)
    def preorder(self, node=None):
        if node is None:
            node = self.root
        if node is not None:
            print(node.data, end = " ")
            if node.left is not None:
                self.preorder(node = node.left)
            if node.right is not None:
                self.preorder(node = node.right)
    def postorder(self, node = None):
        if node is None:
            node = self.root
        if node is not None:
            if node.left is not None:
                self.postorder(node = node.left)
            if node.right is not None:
                self.postorder(node = node.right)
            print(node.data, end = " ")
    def levelorder(self, node = None, level = "1"):
        if node is None:
            node = self.root
            self.dict_ = dict()
        if node is not None:
            if level in self.dict_:
                self.dict_[int(level)].append(node.data)
            else:
                self.dict_[int(level)] = [node.data]
            if node.left is not None:
                self.levelorder(node = node.left, level = int(level) + 1)
            if node.right is not None:
                self.levelorder(node = node.right, level = int(level) + 1)
    def givelevelorder(self):
        print(self.dict_)
        count = 0
        while True:
            flag = 0
            count += 1
            print(f"level:{count}")
            if count in self.dict_:
                flag = 1
                print(self.dict_[count])
            else:
                break
    def print_(self):
        print()
        s = self.root
        print(s.data)
        l1 = s.left
        l2 = s.right
        print(l1.data,l2.data)
        l3 = l1.left
        l4 = l1.right
        l5 = l2.left
        l6 = l2.right
        print(l3.data,l4.data,l6.data)
    def BFStraverse(self):
        pass
    def DFStraverse(self):
        pass
B = BSTree()
B.makeBSTree()
B.Inorder()
print()
#B.preorder()
print()
#B.postorder()
#B.print_()
B.levelorder()
B.givelevelorder()

B.right_pop()
B.levelorder()
B.givelevelorder()
B.right_pop()
B.levelorder()
B.givelevelorder()
#B.delete_(10)
#B.levelorder()
#B.givelevelorder()
print("level deletion")
B.level_delete()
B.levelorder()
B.givelevelorder()
B.level_delete()
B.levelorder()
B.givelevelorder()
B.level_delete()
B.levelorder()
B.givelevelorder()
B.level_delete()
B.levelorder()
B.givelevelorder()