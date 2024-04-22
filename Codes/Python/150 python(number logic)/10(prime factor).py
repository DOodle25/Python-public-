class prime:
    def prime(self,n):
        self.n = n
        for i in range(2,int((n/2)+1)):
            if n % i == 0:
                return False
        return True
    def prime_factors(self,n):
        l = [1,]
        for j in range(2,int((n/2)+1)):
            if n % j == 0:
                if(self.prime(j)):
                    l.append(j)
        return l

obj = prime()
print(obj.prime_factors(int(input("Enter the number : "))))