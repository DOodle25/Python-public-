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
    def N_by_2_cealing(self,bt):
        btlen = int(self.length_of_int(bt))
        if btlen % 2 == 0:
            return int((btlen-1)/2)
        else:
            return int(btlen/2)
    def range_generator(self,size):
        self.size = size
        start = 1 * (10 ** self.size)
        end = 1 * (10 ** (self.size + 1))
        return start,end

    def perfect_square(self,num):
        self.num = num
        cealing = self.N_by_2_cealing(self.num)
        x,y = self.range_generator(cealing)
        for i in range(x,y):
            if num == (i*i):
                return True
        return False
    def is_sunny(self,num):
        self.x = num
        if self.x == 0:
            return False
        newnum = self.x+ 1
        return self.perfect_square(newnum)
    #def is_range_sunny(self,a,b):
        #self.a = a
        #self.b = b
        #for i in range(a, b + 1):
            #if(self.is_sunny(i)):
                #print(f"{i} is sunny number")
    def is_nth_sunny(self, n):
        count = 0
        i = 1
        while True:
            if self.is_sunny(i):
                count += 1
            if count == n:
                print(f"The {n} position sunny number is: {i}")
                break
            i += 1

                

math_object = math_fucntions()
#math_object.is_range_sunny(int(input("S:")),int(input("E:")))
math_object.is_nth_sunny(int(input("Nth:")))