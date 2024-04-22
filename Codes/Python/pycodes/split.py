#class for functions
class math_fucntions:
    #function to find the length of an integer
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
    #function to find power of given number with a given power
    def power(self,num,pwr):
        self.num = num
        self.pwr = pwr
        if self.pwr == 0:
            return 1
        while self.pwr != 1:
            self.num *= num
            self.pwr -= 1
        return self.num
    #123 , 45 ---> 12345
    def add_at_last(self,num,add_num):
        self.num = num
        self.add_num = add_num
        if self.num == 0:
            print("trying to add numbers behind 0 not possible in integer format")
            return
        if self.add_num < 0:
            print("trying to add negitive number behind positive not possible in integer format")
            return
        return (self.num*(self.power(10,self.length_of_int(self.add_num))) + self.add_num)
    #123 , 45 ---> 145
    def replace_at_last(self,num,add_num):
        self.num = num
        self.add_num = add_num
        if self.add_num < 0:
            print("trying to add negitive number behind positive is not possible in integer format")
            return
        #x = (self.num//self.power(10,self.length_of_int(self.add_num)))
        #y = (self.power(10,self.length_of_int(add_num)))
        #print((self.num//self.power(10,self.length_of_int(self.add_num))))
        #print((self.power(10,self.length_of_int(self.add_num))))
        #print((self.num//self.power(10,self.length_of_int(self.add_num)))*(self.power(10,self.length_of_int(self.add_num))))
        #return ((self.num//self.power(10,self.length_of_int(self.add_num))) * (self.power(10,self.length_of_int(add_num)))) + self.add_num
        x = (self.num//self.power(10,self.length_of_int(self.add_num)))
        y = (self.power(10,self.length_of_int(self.add_num)))
        return ((x) * (y)) + self.add_num
    def split_number(self,num,split_point):
        self.num1 = num
        self.num2 = num
        self.split_point1 = split_point
        if split_point < 1 or split_point >= (self.length_of_int(self.num1)):
            print("cannot split a number before it starts or after it ends")
        return (self.num1 // self.power(10,self.length_of_int(self.num2) - self.split_point1)),(self.num2 % self.power(10,self.length_of_int(self.num2) - self.split_point1))
    
math_object = math_fucntions()
#print(math_object.split_number(1234567,5))