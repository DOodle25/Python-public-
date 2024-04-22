class sum_:
    def sum_(self,a,b):
        self.a = a
        self.b = b
        while b != 0:
            c = a & b
            a = a ^ b
            b = c << 1
        return a
obj = sum_()
sum_val = obj.sum_(int(input("A:")),int(input("B:")))
print(sum_val)
print(29 ^ 36)