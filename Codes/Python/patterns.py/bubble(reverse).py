def bubble(arr,len_):
    pre_arr = list(arr)
    for i in range(len_ - 1):
        for j in range(len_ - 1, i, -1):
            flag = True
            if arr[j] < arr[j - 1]:
                flag = False
                arr[j],arr[j - 1] = arr[j - 1],arr[j]
        if flag:
            return pre_arr, "------>", arr
    return pre_arr,arr

print(*bubble([2,7,4,9,1,8,1],7))