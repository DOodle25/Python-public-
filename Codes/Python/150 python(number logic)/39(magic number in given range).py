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
    def reverse(self,n):
        self.n = n
        l = self.integer_to_list(n)
        sum = 0
        j = 0
        for i in l:
            sum = sum + (int(i)*(10**j))
            j+=1
        return sum
    def is_magic(self,num):
        self.x = num
        len_ = self.length_of_int(self.x)
        l = self.integer_to_list(self.x)
        sum = 0
        for i in l:
            sum += i 
        rev = self.reverse(sum)
        return num == rev*sum
    def is_range_magic(self,a,b):
        self.a = a
        self.b = b
        for i in range(a, b + 1):
            if(self.is_magic(i)):
                print(f"{i} is magic number")
    #def is_nth_magic(self, n):
        #count = 0
        #i = 1
        #while True:
            #if self.is_magic(i):
                count += 1
            #if count == n:
                #print(f"The {n} position magic number is: {i}")
                #break
            #i += 1

                

math_object = math_fucntions()
math_object.is_range_magic(int(input("S:")),int(input("E:")))
#math_object.is_nth_magic(int(input("Nth:")))