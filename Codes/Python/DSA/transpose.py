A =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#A =[[1,2,3],[4,5,6],[7,8,9]]
n = len(A)
rot = int(input("enter the number of rotations : "))
for k in range(0, rot):
    for i in range(1, n):
        for j in range(0, i):
            A[i][j], A[j][i] = A [j][i], A[i][j]
    for i in range(0, n):
        for j in range(0, n//2):
            A[i][j], A[i][n - j - 1] = A [i][n - j - 1], A[i][j]
print(A[0])
print(A[1])
print(A[2])
print(A[3])