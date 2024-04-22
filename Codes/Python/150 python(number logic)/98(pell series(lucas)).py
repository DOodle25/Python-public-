class pell:
    def pell_number(self, n):
        self.x = [0, 1]  
        while len(self.x) < n:
            l = 2*(self.x[-1]) + self.x[-2]
            self.x.append(l)
        return self.x
    def n_pell_number(self, n):
        print(f"First {n} pell numbers: {self.pell_number(n)}")


pell_object = pell()
n = int(input("N: "))
pell_object.n_pell_number(n)
