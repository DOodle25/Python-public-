a = list()
n = int(input())
for i in range(n):
    temp_l = list()
    for j in range(n):
        temp_l.append(int(input()))
    a.append(temp_l)
print(a)
move = 1
odd_even = 
for k in range(((n + 1)//2)):
    for l in range(n - 1 , 0, -2):
        if move == 1:
            print(a[i][j], end = " ")
            move = 2
        elif move == 2:
            print(a[i][j], end = " ")
            move = 3
        elif move == 3:
            print(a[i][j], end = " ")
            move = 4
        elif move == 4:
            print(a[i][j], end = " ")
            move = 5
        
    