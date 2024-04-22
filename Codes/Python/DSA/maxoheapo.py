def left(i):
    return 2*i


def right(i):
    return 2*i + 1


def parent(i):
    return i//2


def max_heapify(a, heap_size, i):
    print(i)
    print(a)
    l = left(i)
    r = right(i)

    largest = i 

    if l < heap_size and a[l] > a[i]:
        largest = l
    
    if r < heap_size and a[r] > a[largest]:
        largest = r 
    
    if largest != i:
        # swap elements
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size, largest)


def build_max_heap(a):
    heap_size = len(a)

    for i in range(heap_size//2, 0, -1):
        max_heapify(a, heap_size, i)


def heap_sort(a):
    build_max_heap(a)

    for i in range(len(a)-1, 1, -1):
        a[i], a[1] = a[1], a[i]


        max_heapify(a, i, 1)


def main():


    a = [None,1,2,3,4,5]
    heap_sort(a)
    print(a[1:])

    a = [None, 3, 9, 2, 1]
    heap_sort(a)
    print(a[1:])


main()