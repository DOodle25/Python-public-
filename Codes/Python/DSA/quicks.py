def pos(a,s,e):
        i=s-1
        for j in range(s,e+1):
                if a[j]<a[e]:
                        i=i+1
                        a[i],a[j]=a[j],a[i]
        i=i+1
        a[i],a[e]=a[e],a[i]
        print(i)
        return i
def qsort(a,s,e):
        if s<e:
            m=pos(a,s,e)
            qsort(a,s,m-1)
            qsort(a,m+1,e)
        return a
a=[6,5,4,3,2,1,9]
print(qsort(a,0,len(a)-1))