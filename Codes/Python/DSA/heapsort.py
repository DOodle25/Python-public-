def heapsort(A):
    for i in range((len(A) // 2) - 1, -1, -1):
        heapify(A, i, len(A))
    for j in range(len(A) - 1, 0, -1):
        A[0], A[j] = A[j], A[0]
        heapify(A, 0, j)
    return A

def heapify(A, i, size):
    mx = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < size and A[l] > A[mx]:
        mx = l
    if r < size and A[r] > A[mx]:
        mx = r
    if not mx == i:
        A[i], A[mx] = A[mx], A[i]
        heapify(A, mx, size)

A = [10, 2, 56, 7, 7, 8, 2, 0, 90, 1000, 0, 30]
print(heapsort(A))