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
    def power(self,num,pwr):
        self.num = num
        self.pwr = pwr
        if self.pwr == 0:
            return 1
        while self.pwr != 1:
            self.num *= num
            self.pwr -= 1
        return self.num
    def isdisarium(self,n):
        self.n = n
        l = self.integer_to_list(n)
        len_ = int(1)
        sum = int(0)
        for i in l:
            sum = sum + self.power(i,len_)
            print(sum)
            len_ += 1
        return sum == n
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

math_object = math_fucntions()
n = (int(input("N:")))
b = math_object.is_happy(n)
c = math_object.isdisarium(n)
if(b == True):
    print("its not an unhappy number")
else:
    print("its an unhappy number")
if(c == True):
    print("its not an disarium number")
else:
    print("its an disarium number")