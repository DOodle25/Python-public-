class Adding:
    def __init__(self,data):
        self.data = data
    def __add__(val1,val2):
            l = Adding([0]*len(val1.data))
            for i in range(len(val1.data)):
                l.data[0] = val1.data
                l.data[1] = val2.data
            return l
        #val1.added = [0] * 2
        #val1.added[0] = val1.data
        #val1.added[1] = val2.data
        #return val1.added
a = Adding({1,2,3})
b = Adding([5,6])
c = Adding((9,10))
d = Adding(9)
e = Adding(8)
print((type(a + b + c + d + e)))
print((a + b + c + d + e).data)