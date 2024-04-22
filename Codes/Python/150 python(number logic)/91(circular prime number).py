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
    def all_cicular(self,m):
        self.m = m 
        len_ = self.length_of_int(self.m)
        l = self.integer_to_list(self.m)
        fl = list()
        #print(len_,l)
        u = 0
        for i in range (len_):
            sum_ = 0
            v = 0
            for j in range (len_):
                #print(f"u:{u}")
                sum_ += l[j-u] * (10 ** v)
                v += 1
            u += 1
            #print(f"sum:{sum_}")
            fl.append(sum_)
        #print(fl)
        return fl
    def is_circular_prime(self,nm):
        if self.is_prime(nm):
            list_ = self.all_cicular(nm)
            for i in list_:
                if not(self.is_prime(i)):
                    return False
        else :
            return False
        return True

math_object = math_fucntions()
for i in range (0,100):
    print(f"{i}:{math_object.is_circular_prime(i)}")
#print(math_object.is_circular_prime(int(input("N:"))))