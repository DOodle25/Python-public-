def countSort(arr):
    m=-1
    l=len(arr)
    cp=[-1]*n
    for i in range(0,n):
        if arr[i]>m:
            m=arr[i]
        cp[i]=arr[i]

    k=[0]*(m+1)

    for i in arr:
        k[i]+=1

    for i in range(1,m+1):
        k[i]+=k[i-1]

    for i in range(n-1,-1,-1):
        k[cp[i]]-=1
        arr[k[cp[i]]]=cp[i]


countSort(arr)
print(arr)