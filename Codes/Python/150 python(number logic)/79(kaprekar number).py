import math
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
    def is_kaprekar(self,m):
        if m == 0:
            return False
        self.m = m
        self.m = m*m
        l = self.integer_to_list(self.m)
        sum_ = 0
        len_ = self.length_of_int(self.m)
        #print(len_)
        n1 = self.m // (10**int(math.ceil((len_/2))))
        n2 = self.m % (10**int(math.ceil((len_/2))))
        #print(n1,n2)
        return (n1 + n2) == m
    def is_range_kaprekar(self,a,b):
        self.a = a
        self.b = b
        for i in range(a, b + 1):
            if(self.is_kaprekar(i)):
                print(f"{i} is kaprekar number")

math_object = math_fucntions()
math_object.is_range_kaprekar(0,1000)
#math_object.is_range_kaprekar(9,9)

