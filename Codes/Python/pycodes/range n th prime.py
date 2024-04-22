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
        if n == 0 or n == 1 :
            return False
        self.n = n
        for i in range(2,int((n/2)+1)):
            if n % i == 0:
                return False
        return True
    def is_stupid_prime(self,n):
        self.n = n
        l = self.integer_to_list(n)
        for i in l:
            if (not(self.is_prime(i))):
                return False
        return True
    def is_range_prime(self,a,b,n):
        self.a = a
        self.b = b
        self.n = n
        count = 0
        for i in range(a, b + 1):
                if self.is_stupid_prime(i):
                    count += 1
                if count == n:
                    print(f"The {n} position prime number is: {i} in range {a} to {b}")
                    break
               

math_object = math_fucntions()
print(73%1)
math_object.is_range_prime(int(input("S:")),int(input("E:")),int(input("N:")))