class prime:
    def prime(self,n):
        self.n = n
        for i in range(2,int((n/2)+1)):
            if n % i == 0:
                return False
        return True
obj = prime()
print(obj.prime(int(input("Enter the number : "))))