class math_fucntions:
    def is_number_present(self, num, l):
        return num in l
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
    def is_happy(self,num):
        #list to check repeat number
        self.x = num
        lc = [0,]
        len_ = self.length_of_int(self.x)
        while (not(self.is_number_present(self.x,lc))):
            lc.append(self.x)
            #print(lc)
            sum = self.x
            l = self.integer_to_list(sum)
            sum = 0
            for i in l:
                sum = sum + i**2
            len_ = self.length_of_int(sum)
            self.x = sum
            if self.x == 1:
                return True
        return False
    #def is_range_happy(self,a,b):
        #self.a = a
        #self.b = b
        #for i in range(a, b + 1):
            #if(self.is_happy(i)):
                #print(f"{i} is happy number")
    def is_nth_happy(self, n):
        count = 0
        i = 1
        while True:
            if self.is_happy(i):
                count += 1
            if count == n:
                print(f"The {n} position happy number is: {i}")
                break
            i += 1

                

math_object = math_fucntions()
#math_object.is_range_happy(int(input("S:")),int(input("E:")))
n = (int(input("N:")))
for i in range(1,n+1):
    math_object.is_nth_happy(i)