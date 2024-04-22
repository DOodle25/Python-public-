#traverse insertion deletion search update
import array as arr
a = arr.array('i',[1,2,3,4,5])
#1. adding an element in array 1>insert() -extends on the location(LOCATION,ELEMENT)(if out of bound adds at the end) 2>append()
print(a)
a.insert(10,7)
print(a)
a.append(8)
print(a)
#2. accessing element
b = arr.array('u',['P','A','R','U','L',' ','U','N','I','V','E','R','C','I','T','y'])
print(b)
print(b[0],a[2])
#3. removing element 1>remove(ELEMENT) 2>pop -----> pops last element
b.remove('R')
print(b)
b.pop()
print(b)
#4. traversing and serching
print(a.index(2))
#5. sorting a.srot()
#6. reverse a.reverse()
#7. a.extend() --------> doesnt extend as a new part entends the smae thing
a.extend([1,2,3])
print(a)
#8.count()
print(b.count("I"))
#9.clear() --------> removes all elements and makes new empty array
print(b)
def clear_array(b):
    b = arr.array('i')
    return b
print(b)
b = clear_array(b)
print(b)
#10.combine two array
d = arr.array('i',[10,20,30,40,50])
def combine_two(a,b):
    return a + d
c = combine_two(a,b)
print(c)
for i in range(0,max(len(a),len(b))):
    e = arr.array('i')
print(e)
#11.adding two arrays
a = arr.array('i',[1,2,3,4,5])
b = arr.array('i',[1,2,3,4,5])

f = arr.array('i',[x + y for x,y in zip(a,b)]) 
print(f)
#12.multiplying two arrays
a = arr.array('i',[1,2,3,4,5])
b = arr.array('i',[1,2,3,4,5])

f = arr.array('i',[x * y for x,y in zip(a,b)]) 
print(f)
