def bisearch(n, arr):
    if n in arr:
        return arr.index(n)
    else:
        return -2
    

def readdata(location):
    with open(location) as f:
        n = f.readline()
        m = f.readline()
        arr = f.readline()
        sam = f.readline()
    
    return n, m, arr, sam

def main():
    n, m, arr, sam = readdata('rosalind_bins (2).txt')
    res = ''
    sam = sam.split()
    arr = arr.split()
    for i in sam:
        res += str(bisearch(str(i), arr) + 1) + ' '
    
    with open('test.txt', 'w') as f:
        f.write(res)

main()
