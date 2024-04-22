class Rotation():
    # right to left[ ] if last comes to first
    def __init__(self):
        self.arr = input().split()
        self.len_ = len(self.arr)
        self.no = int(input()) % self.len_
    def reverse(self,arr,s,e):
        while(s<e):
            self.arr[s], self.arr[e]=self.arr[e], self.arr[s]
            s += 1
            e -= 1
    def rotate1(self):
        self.reverse(self.arr,0,self.len_ - self.no - 1)
        self.reverse(self.arr,self.len_ - self.no, self.len_ - 1)
        self.reverse(self.arr,0,self.len_ - 1)
        return self.arr
    def rotate2(self):
        self.reverse(self.arr,0,self.len_ - 1)
        self.reverse(self.arr,0,self.len_ - self.no - 1)
        self.reverse(self.arr,self.len_ - self.no, self.len_ - 1)
        return self.arr

print(Rotation().rotate1())