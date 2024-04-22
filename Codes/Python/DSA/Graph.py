class Node:
    data = 0
    points = []
    costs = []
    def __init__(self, data, points, costs):
        self.data = data
        self.points = points
        self.costs = costs
class Graph:
    root = None
    count = 0

    def insert(self):
        data = input()
        points = input()
        costs = input()
        for i in range(len(input_)):
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
            if root == None:
                root = 