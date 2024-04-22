def buildmaxheap(A):
    for i in range((len(A) // 2) - 1, -1, -1):
        heapifymaxheap(A, i, len(A))
    return A

def heapifymaxheap(A, i, size):
    mx = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < size and A[l] > A[mx]:
        mx = l
    if r < size and A[r] > A[mx]:
        mx = r
    if not mx == i:
        A[i], A[mx] = A[mx], A[i]
        heapifymaxheap(A, mx, size)

def buildminheap(A):
    for i in range((len(A) // 2) - 1, -1, -1):
        heapifyminheap(A, i, len(A))
    return A

def heapifyminheap(A, i, size):
    m = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < size and A[l] < A[m]:
        m = l
    if r < size and A[r] < A[m]:
        m = r
    if not m == i:
        A[i], A[m] = A[m], A[i]
        heapifyminheap(A, m, size)

A = [53,69,33,56,44,52,20]
print(buildmaxheap(A))

A = [53,69,33,56,44,52,20]
print(buildminheap(A))