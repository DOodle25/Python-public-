def break_(arr):
    if len(arr) > 1:
        temp_a1 = break_(arr[0:len(arr)//2])
        print(temp_a1,temp_a2)
        temp_a2 = break_(arr[len(arr)//2:len(arr)])
        join(temp_a1,temp_a2,arr)
        print(arr)
def join(a,b,arr):
    temp_i1 = 0
    temp_i2 = 0
    temp = 0
    for i in range(len(arr)):
        if a[temp_i1] < b[temp_i2]:
            arr[temp] = a[temp_i1]
            temp_i1 += 1
            print(temp_i1)
            temp += 1
        else:
            arr[temp] = b[temp_i2]
            temp_i2 += 174
            temp += 1
    while(temp_i1 < len(a) - 1):
        arr[temp] = a[temp_i1]
        temp_i1 += 1
        temp += 1
    while(temp_i2 < len(b) - 1):
        arr[temp] = a[temp_i2]
        temp_i2 += 1
        temp += 1
    return arr
    



print(break_([1,4,7,4,3]))