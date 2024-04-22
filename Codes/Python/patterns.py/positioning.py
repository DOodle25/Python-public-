def rec_max(arr, k, n, k_ind):
    if(n > len(arr)):
        return
    rec_min(arr, k, n + 1)
def rec_min(arr, k, n, k_ind):
    if(arr[n] == k):
        return
    if arr[n] > k:
        arr[k_ind] = arr[n]
        for i in range(n,k_ind):
            arr[i] = arr[i + 1]
    rec_min(arr, k, n + 1)
def rec(arr, k, n):
    k_ind = arr.index(k)
    if not arr.index(k) == 0:
        rec_min(arr, k, n, k_ind)
    if not arr.index(k) == len(k) - 1:
        rec_max(arr, k, n, k_ind)
        
a = [5,7,4,10,12,19,20,5]
rec(a, 10, 0)