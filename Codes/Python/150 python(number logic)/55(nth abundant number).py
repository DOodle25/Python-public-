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
    #def is_range_abundant(self,a,b):
        #self.a = a
        #self.b = b
        #for i in range(a, b + 1):
            #if(self.is_abundant(i)):
                #print(f"{i} is abundant number")
    def is_nth_abundant(self, n):
        count = 0
        i = 1
        while True:
            if self.is_abundant(i):
                count += 1
            if count == n:
                print(f"The {n} position abundant number is: {i}")
                break
            i += 1

                

math_object = math_fucntions()
#math_object.is_range_abundant(int(input("S:")),int(input("E:")))
math_object.is_nth_abundant(int(input("Nth:")))