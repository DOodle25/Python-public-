order = "cba"
s = "abca"
l = str()
for i in order:
    print(i)
    if i in s:
        l = l + str(i*s.count(i))
        print(l)
        order = order[1:]
        for k in range(s.count(i)):
            s = str((list(s).remove(i)))
if s:
    print(l + s)
else:
    print(l)