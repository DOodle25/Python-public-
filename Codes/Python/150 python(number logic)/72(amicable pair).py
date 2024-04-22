class math_fucntions:
    def length_of_int(self,n):
        self.n = n
        i = int(0)
        if self.n == 0:
            return 1
        if self.n < 0:
            self.n *= -1
        while self.n:
            self.n //= 10
            i += 1
        return i
    def integer_to_list(self,n):
        self.n = n
        len_ = self.length_of_int(n)
        l = [0] * len_
        for j in range(0,self.length_of_int(n)):
            l[len_ - j - 1] = n % 10
            n //= 10
        return l
    def factors(self,n):
        l = [1,]
        for j in range(2,int((n/2)+1)):
            if n % j == 0:
                l.append(j)
        return l
    def amicable(self, n,m):
        self.n = n
        self.m = m
        l = self.factors(n)
        sum_ = 0
        for i in l:
            sum_ = sum_ + i
        return sum_ == m
        
math_object = math_fucntions()
print(math_object.amicable(int(input("N:")),int(input("M:")))),