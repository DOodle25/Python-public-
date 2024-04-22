class LucasNumbers:
    def lucas_number(self, n):
        self.x = [2, 1]  
        while len(self.x) < n:
            l = self.x[-1] + self.x[-2]
            self.x.append(l)
        return self.x
    def n_lucas_number(self, n):
        print(f"First {n} Lucas numbers: {self.lucas_number(n)}")


lucas_object = LucasNumbers()
n = int(input("N: "))
lucas_object.n_lucas_number(n)
