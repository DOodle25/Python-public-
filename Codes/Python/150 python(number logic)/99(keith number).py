class MathFunctions:
    def length_of_int(self, n):
        i = int(0)
        if n == 0:
            return 1
        if n < 0:
            n *= -1
        while n:
            n //= 10
            i += 1
        return i

    def integer_to_list(self, n):
        len_ = self.length_of_int(n)
        l = [0] * len_
        for j in range(0, self.length_of_int(n)):
            l[len_ - j - 1] = n % 10
            n //= 10
        return l

    def is_prime(self, n):
        if n == 1 or n == 0:
            return False
        if (n != 2 and n % 2 == 0) or (n != 3 and n % 3 == 0):
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True

    def factors(self, n):
        l = [1, ]
        for j in range(2, int((n/2)+1)):
            if n % j == 0:
                l.append(j)
        return l

    def is_keith_number(self, num):

math_obj = MathFunctions()
print(math_obj.is_keith_number(int(input("Enter X: "))))
