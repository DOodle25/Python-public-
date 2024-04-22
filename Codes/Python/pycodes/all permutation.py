def swap_list(a,b,num_list):
    print(num_list[a])
    temp = num_list[a]
    num_list[a] = num_list[b]
    num_list[b] = temp
    return num_list
def length_of_int(n):
    n = n
    i = int(0)
    if n == 0:
        return 1
    if n < 0:
        n *= -1
    while n:
        n //= 10
        i += 1
    return i
def integer_to_list(n):
    n = n
    len_ = length_of_int(n)
    l = [0] * len_
    for j in range(0,length_of_int(n)):
        l[len_ - j - 1] = n % 10
        n //= 10
    return l
def all_permutations(a,b,num_list):
    if(a == b):
        return
    else:
        print(num_list)
        num_list = swap_list(a,b,num_list)
        print(num_list)
        lall_permutations(a,b-1,num_list)

all_permutations([1,2,3],0,3)