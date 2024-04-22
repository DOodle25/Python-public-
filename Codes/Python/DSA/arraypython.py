import array as arr
#creating an array of integers
a = arr.array('i',[1,2,3,4,5,])
print(a,id(a))

#creatig an array of floating-point numbers
b = arr.array('f',[0.1,0.2,0.3,0.4,0.5])
print(b)

print(a.itemsize)
print(len(a))