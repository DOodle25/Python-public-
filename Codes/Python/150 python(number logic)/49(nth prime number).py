class math_fucntions:
    def is_prime(self,n):
        self.n = n
        if (self.n != 2 and self.n % 2 == 0) or ( self.n!= 3 and self.n % 3 == 0):
            return False
        i = 5
        while i * i <= self.n:
            if self.n % i == 0 or self.n % (i + 2) == 0:
                return False
            i = i + 6
        return True
    #def is_range_prime(self,a,b):
        #self.a = a
        #self.b = b
        #for i in range(a, b + 1):
            #if(self.is_prime(i)):
                #print(f"{i} is prime number")
    def is_nth_prime(self, n):
        count = 0
        i = 2
        while True:
            if self.is_prime(i):
                count += 1
            if count == n:
                print(f"The {n} position prime number is: {i}")
                break
            i += 1

                

math_object = math_fucntions()
#print(math_object.is_range_prime(int(input("S:")),int(input("E:"))))
math_object.is_nth_prime(int(input("Nth:")))