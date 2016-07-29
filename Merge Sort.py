def readdata(location):
    with open(location) as f:
        tmp = []
        for i in f:
            tmp.append(i.split())
        res = []
        for j in tmp:
            a = []
            if len(j) > 1:
                for k in j:
                    a.append(int(k))
                res.append(a)
    return res[0]

#print readdata('test.txt')

def merge(a, b):
    res = []
    while a and b:
        if a[0] < b[0]:
            res.append(a[0])
            a.pop(0)
        
        else:
            res.append(b[0])
            b.pop(0)
    
    if a:
        res += a
    if b:
        res += b

    return res

def mergesort(arr):
    if len(arr) < 2:
        return arr
    else:
        a = mergesort(arr[:len(arr)/2])
        b = mergesort(arr[len(arr)/2:])
        return merge(a,b)
    


def main():
    a = readdata('rosalind_ms.txt')
    t = mergesort(a)
    res = ''
    for i in t:
        res += str(i) + ' '
    with open('tmp.txt', 'w') as f:
        f.write(res)

main()
    