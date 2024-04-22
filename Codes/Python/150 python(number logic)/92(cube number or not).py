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
    def is_prime(self,n):
        self.n = n
        if self.n == 1 or self.n == 0:
            return False
        if (self.n != 2 and self.n % 2 == 0) or ( self.n!= 3 and self.n % 3 == 0):
            return False
        i = 5
        while i * i <= self.n:
            if self.n % i == 0 or self.n % (i + 2) == 0:
                return False
            i = i + 6
        return True
    def factors(self,n):
        l = [1,]
        for j in range(2,int((n/2)+1)):
            if n % j == 0:
                l.append(j)
        return l
    def is_cube(self,mn):
        self.mn = mn
        fl = self.factors(self.mn)
        for i in fl:
            if (i*i*i == mn):
                return True
        return False

math_object = math_fucntions()
for i in range (0,1000):
    if(math_object.is_cube(i)):
        print(f"{i}:{math_object.is_cube(i)}")
print(math_object.is_cube(int(input("N:"))))
