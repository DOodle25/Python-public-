print("Enter a range:")
range1=int(input())
range2=int(input())
print("Evil numbers between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
    one_c = 0
    num=i
    while num != 0:
        if num % 2 == 1:
            one_c += 1
        num //= 2
    if one_c % 2 == 0:
        print(i,end=" ")
    #def is_magic(self,num):
        #self.x = num
        #len_ = self.length_of_int(self.x)
        #while (len_ != 1):
            #sum = self.x
            #l = self.integer_to_list(sum)
            #sum = 0
            #for i in l:
                #sum = sum + i
            #len_ = self.length_of_int(sum)
            #self.x = sum
        #return self.x == 1

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
    def power(self,num,pwr):
        self.num = num
        self.pwr = pwr
        if self.pwr == 0:
            return 1
        while self.pwr != 1:
            self.num *= num
            self.pwr -= 1
        return self.num
    def factorial(self,n):
        sum = 1
        self.n = n
        if (self.n == 1):
            return 1
        for i in range (2,n+1):
            sum = sum * i
        return sum
    def factors(self,n):
        l = [1,]
        for j in range(2,int((n/2)+1)):
            if n % j == 0:
                l.append(j)
        l.append(n)
        return l
    def is_pronic(self,n):
        self.n = n
        l = self.integer_to_list(n)
        f = self.factors(n)
        fl = int(len(f))
        j = 0
        for i in range(0,fl-1):
            if (f[i] + 1) == f[i+1]:
                if f[i]*f[i+1] == n:
                    return True
                j += 1
        return False
    #def is_range_pronic(self,a,b):
        #self.a = a
        #self.b = b
        #for i in range(a, b + 1):
            #if(self.is_pronic(i)):
                #print(f"{i} is pronic number")
    def is_nth_pronic(self, n):
        count = 0
        i = 1
        while True:
            if self.is_pronic(i):
                count += 1
            if count == n:
                print(f"The {n} position pronic number is: {i}")
                break
            i += 1

math_object = math_fucntions()
#math_object.is_range_disarium(int(input("S:")),int(input("E:")))
math_object.is_nth_disarium(int(input("Nth:")))