import array as arr
a = arr.array('u',['P','A','R','U','L',' ','U','N','I','V','E','R','S','I','T','Y'])
print(a)
j,k = ['P'],[]
for i in a:
    for l in j:
        if i == l:
            k[j.index(l)] += 1
        else:
            j.append(i)
            k.append(int(1))
        
print(j)
print(k)

