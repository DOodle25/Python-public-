def reverse_(str_):
    len_ = len(str_)
    z = str()
    for j in range(len_):
        z = z + str_[len_ - j - 1]
    str_ = z
    return str_ 
def reverse_portion(str_):
    len_ = len(str_)
    z = str()
    temp = 0
    for i in range(len_):
        temp += 1
        if str_[i] == " ":
            for j in range(i - 1, i - temp , -1):
                z = z + str_[j]
            temp = 0
            z = z + " "
    if not str_[len_ - 1] == " ":
        for k in range(len_ - 1, len_ - temp - 1, -1):
                z = z + str_[k]
    str_ = z
    return str_ 
def p1(str_):
    len_ = len(str_)
    z = str()
    temp = 0
    for i in range(len_):
        temp += 1
        if str_[i] == " ":
            #for j in range(i - 1, i - temp , -1):
            for j in range(i - temp + 1, i):
                if j == i - temp + 1:
                    z = z + "#"
                elif j == i - 1:
                    z = z + "@"
                else:
                    z = z + str_[j]
            temp = 0
            z = z + " "
    if not str_[len_ - 1] == " ":
        for k in range(i - temp + 1, i + 1):
            if k == i - temp + 1:
                z = z + "#"
            elif k == i :
                z = z + "@"
            else:
                z = z + str_[k]
    str_ = z
    return str_ 
def p2(str_):
    len_ = len(str_)
    z = str()
    temp = 0
    for i in range(len_):
        temp += 1
        if str_[i] == " ":
            #for j in range(i - 1, i - temp , -1):
            for j in range(i - temp + 1, i):
                if j == i - temp + 1:
                    z = z + (chr(35 + (ord(str_[j]))))
                elif j == i - 1:
                    z = z + (chr(35 + (ord(str_[j]))))
                else:
                    z = z + str_[j]
            temp = 0
            z = z + " "
    if not str_[len_ - 1] == " ":
        for k in range(i - temp + 1, i + 1):
            if k == i - temp + 1:
                z = z + (chr(35 + (ord(str_[j]))))
            elif k == i :
                z = z + "@"
            else:
                z = z + (chr(35 + (ord(str_[j]))))
    str_ = z
    return str_ 
#print(reverse_(str(input())))
#print(reverse_portion(str(input())))
print(p2(str(input())))