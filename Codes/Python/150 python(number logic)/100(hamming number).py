class math_fucntions:
    def is_prime(self,n):
        self.n = n
        if (self.n == 1 or self.n == 0):
            return False
        if (self.n != 2 and self.n % 2 == 0) or ( self.n!= 3 and self.n % 3 == 0):
            return False
        i = 5
        while i * i <= self.n:
            if self.n % i == 0 or self.n % (i + 2) == 0:
                return False
            i = i + 6
        return True

    def is_hamming(self, n):
        self.n = n
        x = True
        if n == 0:
            return False
        if len(str(n)) <= 1 and len(str(n)) >= 0:
            return True
        if self.is_prime(n):
            return False
        else :
            n = int(n)
            for i in range (1,int(n/2)+1):
                if n % i == 0:
                    if self.is_prime(i):
                        if i == 2 or i == 3 or i == 5:
                            x = True
                        else:
                            return False
            return x

                

math_object = math_fucntions()
for j in range(0,40):
    #print(math_object.is_hamming(int(input("Nth:"))))
    print(f"{j}:{math_object.is_hamming(j)}",end=' ')
