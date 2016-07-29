def readdata(location):
    with open(location) as f:
        n = f.readline()
        arr = f.readline()
    temp = []
    for i in arr.split():
        temp.append(int(i))
    return n, temp


def insort(arr):
    res = 0
    for i in xrange(len(arr) - 1):
        for j in xrange(len(arr) - 1):
            if arr[j] > arr[j+1]:
                res += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return res

def main():
    n, arr = readdata('rosalind_ins.txt')
    #print arr
    print insort(arr)
    

main()

#print readdata('test.txt')