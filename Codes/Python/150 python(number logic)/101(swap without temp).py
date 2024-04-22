a,b = 10,20
print(a,b)
a,b = b,a
print(a,b)
a += b
b = a - b
a -= b
print(a,b)