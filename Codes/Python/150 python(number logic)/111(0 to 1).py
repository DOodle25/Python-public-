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
    def replace_zeros_with_one(self,num):
        l = self.integer_to_list(num)
        len_ = self.length_of_int(num)
        for i in range(0,len_):
            if l[i] == 0:
                l[i] = 1
        sum_ = 0
        for i in range(0,len_):
            sum_ += l[i] * (10**(len_-i-1))
        return sum_

math_obj = math_fucntions()
print(math_obj.replace_zeros_with_one(int(input("N:"))))