class math_functions:
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

    #function to find the length of an integer
    def perfect_square(self,num):
        self.num = num
        cealing = self.N_by_2_cealing(self.num)
        x,y = self.range_generator(cealing)
        for i in range(x,y):
            if num == (i*i):
                return True
        return False
    def issunny(self,num):
        self.x = num
        if self.x == 0:
            return False
        newnum = self.x+ 1
        return self.perfect_square(newnum)

math_object = math_functions()
print(math_object.issunny(int(input("Enter the integer:"))))