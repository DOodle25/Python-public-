class student:
    name = "surya"
    age = 19
    score = 8.9
    def performance():
        marks = [int(i) for i in input().split()]
        total = marks[0] + marks[1] + marks[2]
        print("total Score of ",student.name,"is",total)
        s = "10 20 30"
        x = s.rsplit()
        print(x)

student.performance()