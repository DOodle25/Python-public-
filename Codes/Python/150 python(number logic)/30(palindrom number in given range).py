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
    def is_palindrome(self,n):
        l = self.integer_to_list(n)
        len_ = self.length_of_int(n)
        for i in range(0,len_):
            if(l[i] != l[len_ - i -1]):
                return False
        return True
    def is_range_palindrome(self,a,b):
        self.a = a
        self.b = b
        for i in range(a, b + 1):
            if(self.is_palindrome(i)):
                print(f"{i} is palindrome number")
    #def is_nth_palindrom(self, n):
        #count = 0
        #i = 1
        #while True:
            #if self.is_palindrome(i):
                #count += 1
            #if count == n:
                #print(f"The {n} position palindrome number is: {i}")
                #break
            #i += 1 

math_object = math_fucntions()
math_object.is_range_palindrome(int(input("S:")),int(input("E:")))
#math_object.is_nth_palindrom(int(input("Nth:")))