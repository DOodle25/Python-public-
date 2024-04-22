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


math_object = math_fucntions()
print(math_object.reverse(int(input("Enter the integer:"))))