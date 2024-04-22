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
    def is_disarium(self,n):
        self.n = n
        l = self.integer_to_list(n)
        len_ = int(1)
        sum = int(0)
        for i in l:
            sum = sum + self.power(i,len_)
            #print(sum)
            len_ += 1
        return sum == n
    def is_range_disarium(self,a,b):
        self.a = a
        self.b = b
        for i in range(a, b + 1):
            if(self.is_disarium(i)):
                print(f"{i} is disarium number")
    #def is_nth_disarium(self, n):
        #count = 0
        #i = 1
        #while True:
            #if self.is_disarium(i):
                #count += 1
            #if count == n:
                #print(f"The {n} position disarium number is: {i}")
                #break
            #i += 1

                

math_object = math_fucntions()
math_object.is_range_disarium(int(input("S:")),int(input("E:")))
#math_object.is_nth_disarium(int(input("Nth:")))