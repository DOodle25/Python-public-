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
    def generic_root(self,num):
            self.x = num
            len_ = self.length_of_int(self.x)
            while (len_ != 1):
                sum = self.x
                l = self.integer_to_list(sum)
                sum = 0
                for i in l:
                    sum = sum + i
                len_ = self.length_of_int(sum)
                self.x = sum
            return self.x

                

math_object = math_fucntions()
print(math_object.generic_root(int(input("N:"))))