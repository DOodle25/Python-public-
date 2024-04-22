input_ = input("Enter the height and length with a space :").split(' ')
for it in range(0, len(input_), 2):
        if(input_[it] == "height"):
            height = int(input_[it + 1])
        if(input_[it] == "length"):
            length = int(input_[it + 1])
#height,length = int(input("Height:")),int(input("width:"))
k = height + 1
for i in range(height):
    o = k - i - 1
    s_gap = 0
    for l in range (height - i):
        print(" ",end = " ")
    for j in range(height - i - 1,length + 1):
        if((j+1)%(o) == 0):
            print(j%10,end = " ")
            if s_gap == 0:
                o += i*2 + 1
                s_gap = 1
            else :
                o += (height -i*2) + height - 1
                s_gap = 0
        else:
            print(" ",end = " ") 
    print()
    