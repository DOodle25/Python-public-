class without_operators:
    def sum_(self,a,b):
        self.a = a
        print(f"a:{a}b:{b}")
        self.b = b
        while b != 0:
            print(f"a:{a}b:{b}")
            c = a & b
            a = a ^ b
            b = c << 1
        return a
    def minus_(self,c,d):
        if (c < d):
            c,d = d,c
        self.c = c
        self.d = d
        self.d = self.sum_(e,1)
        e = ~self.d
        print(e)
        print(f"c:{c} e:{e}")
        print(f"c:{c} e:{e}")
        return self.sum_(c,e)
obj = without_operators()
sum_val = obj.minus_(int(input("A:")),int(input("B:")))
print(sum_val)