def readdata(location):
    with open(location) as f:
        n = f.readline()
        arr = map(int,f.readline().split())
    return arr

a = readdata('rosalind_hea.txt')
#print a

def bi_heap(arr):
    #for i in xrange(2, len(arr)):
    #    if arr[i/2] < arr[i]:
    #        arr[i/2], arr[i] = arr[i], arr[i/2]
    a = sorted(arr, reverse = True)
    b = ' '.join([str(i) for i in a])
    with open('res.txt', 'w') as f:
        f.write(b)
    return b

def bi_heap2(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and a[j] > a[(j-1)//2]:
            a[j], a[(j-1)//2] = a[(j-1)//2], a[j]
            j = (j-1)//2
    #print(*arr)
    return arr



print bi_heap2(a)
