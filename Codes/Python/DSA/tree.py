class Node:
    data = 0
    left = None
    right = None
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    root = None
    count = 0
    next_new = None
    def makeTree(self):
        if root == None:
            root = Node(data)
            next_new = root.left
            count += 1
        else:
            count += 1
            next_new = Node(data)