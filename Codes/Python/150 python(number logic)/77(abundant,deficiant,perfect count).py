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
    def power(self,num,pwr):
        self.num = num
        self.pwr = pwr
        if self.pwr == 0:
            return 1
        while self.pwr != 1:
            self.num *= num
            self.pwr -= 1
        return self.num
    def factorial(self,n):
        sum = 1
        self.n = n
        if (self.n == 1):
            return 1
        for i in range (2,n+1):
            sum = sum * i
        return sum
    def factors(self,n):
        l = [1,]
        for j in range(2,int((n/2)+1)):
            if n % j == 0:
                l.append(j)
        return l
    def is_abundant(self,n):
        self.n = n
        len_ = self.length_of_int(n)
        sum = int(0)
        l = self.factors(n)
        for i in l:
            sum = sum + i
        return n < sum
    def is_range_abundant(self,a,b):
        self.a = a
        self.b = b
        c1 = int(0)
        for i in range(a, b + 1):
            if(self.is_abundant(i)):
                c1 += 1
        return c1
    def is_deficient(slef,m):
        self.m = m
        l = self.factors(m)
        sum_ = 0
        for i in l:
            sum_ += i
        return sum_ < m
    def is_range_deficient(self,c,d):
        self.c = c
        self.d = d
        c2 = int(0)
        for i in range(c, d + 1):
            if(self.is_deficient(i)):
                c2 += 1
        return c2

    def is_perfect(self,n):
        self.n = n
        if self.n == 1:
            return False
        len_ = self.length_of_int(n)
        sum = int(0)
        l = self.factors(n)
        for i in l:
            sum = sum + i
        return sum == n
    def is_range_perfect(self,e,f):
        self.e = e
        self.f = f
        c3 = int(0)
        for i in range(a, b + 1):
            if(self.is_perfect(i)):
                print(f"{i} is perfect number")
        return c3

math_object = math_fucntions()
for i in range (0,1000):
    print(f"there are {math_object.is_range_abundant(0,1000)} abundant numbers between 0 to 1000")
    print(f"there are {math_object.is_range_deficient(0,1000)} deficient numbers between 0 to 1000")
    print(f"there are {math_object.is_range_perfect(0,1000)} perfect numbers between 0 to 1000")
