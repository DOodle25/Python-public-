class student:
    def __init__(self, sname, dept, m1, m2, m3):
        self.sname = sname
        self.dept = dept 
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        total = self.m1 + self.m2 + self.m3
        print("name :",self.sname)
        print("Dept :",self.dept)
        print("Total Score :",total)

s1 = student("Sneha","CSE",100,45,67)
s2 = student("Reddy","IT",90,88,77)