class math_fucntions:
    #function to find the length of an integer
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
        l.append(n)
        return l
    def isfriendlypair(self,a,b):
        sum1 = 0
        sum2 = 0
        self.a = a
        self.b = b
        l1 = self.factors(self.a)
        l2 = self.factors(self.b)
        for i in l1:
            sum1 = sum1 + i
        for j in l2:
            sum2 = sum2 + j
        return (sum1/a) == (sum2/b)


math_object = math_fucntions()
print(math_object.isfriendlypair(int(input("X:")),int(input("Y:"))))
