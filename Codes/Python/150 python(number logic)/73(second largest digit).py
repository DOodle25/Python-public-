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
    def slargest(self, n):
        largest = 0
        slargest = 0
        self.n = n
        l = self.integer_to_list(n)
        for i in l:
            if i > slargest and i > largest:
                slargest = largest
                largest = i
            elif i > slargest and i != largest:
                slargest = i
            #print(f"largest:{largest}")
            #print(f"slargest:{slargest}")
        return slargest

math_object = math_fucntions()
print(math_object.slargest(int(input("N:"))))