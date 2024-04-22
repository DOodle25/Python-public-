#class for functions



n = int(input())
m = int(input())
x = len(str(n))
y = len(str(m))
x = int(x/2)
b = int(n % (10**y))
a = int(n / (10**x))
a = int(a * (10**y))
a = int(a + m)
a = int(a * (10**x))
a = int(a + b)
print(a)