h = int(input("Height:"))
for i in range (1,h + 1):
    #print spacing in front
    for m in range (h - i):
        print(" ", end = " ")
    for j in range ((i * 2)-1):
        if(j < int((i * 2) / 2)):
            print(chr(97 + j),end=" ")
        else:
            print(chr(95 + (i * 2) - j), end = " ")
    print()