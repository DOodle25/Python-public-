class math_fucntions:
    def is_range_(self,a,b):
        self.a = a
        self.b = b
        for i in range(a, b + 1):
            if(self.is_(i)):
                print(f"{i} is ?? number")
    def is_nth_(self, n):
        count = 0
        i = 1
        while True:
            if self.is_(i):
                count += 1
            if count == n:
                print(f"The {n} position ?? number is: {i}")
                break
            i += 1

                

math_object = math_fucntions()
math_object.is_range_(int(input("S:")),int(input("E:")))
math_object.is_nth_(int(input("Nth:")))