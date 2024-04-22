class CatalanNumbers:
    def factorial(self,n):
        sum_ = 1
        self.n = n
        if (self.n == 1):
            return 1
        for i in range (2,n+1):
            sum_ = sum_ * i
        return sum_
    def catalan_number(self, n):
        self.n = n
        if self.n == 0:
            return [1]
        else:
            x = [1, 1]
            while len(x) < n:
                y = (self.factorial(2 * self.n)) / (self.factorial(self.n + 1) * self.factorial(self.n))
                x.append(y)
            return x

    def n_catalan_number(self, n):
        print(f"First {n} Catalan numbers: {self.catalan_number(n)}")


catalan_object = CatalanNumbers()
n = int(input("N: "))
catalan_object.n_catalan_number(n)
