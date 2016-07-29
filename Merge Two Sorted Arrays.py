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
    return res

print readdata('rosalind_mer.txt')

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


def main():
    a, b = readdata('rosalind_mer.txt')
    t = merge(a,b)
    res = ''
    for i in t:
        res += str(i) + ' '
    print res

main()
    