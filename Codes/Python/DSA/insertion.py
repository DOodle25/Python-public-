def shift(val,arr,i,j):
    if j == len(arr) - 1:
        arr[j - 1] = arr[j]
        arr[j] = val
    else:
        if(arr[j - 1] < arr[j]):
            arr[j - 1] = arr[j]
            shift(val,arr,i,j + 1)
        else:
            arr[j - 1] = arr[j]
            arr[j] = val

def insertion(arr):
    len_ = len(arr)
    for i in range(len_ - 2, -1, -1):
        shift(arr[i],arr,i,i+1)
    return arr
print(insertion([5,4,3,423,]))     