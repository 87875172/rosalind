def readdata(location):
    with open(location) as f:
        a = f.readline()
        k, n = a.split()
        arr = []
        for i in f:
            temp = []
            for j in i.split():
                temp.append(int(j))
            arr.append(temp)
    return int(k), int(n), arr
        
def tsum(arr):
    su = 100000
    tmp = ''
    for i in xrange(len(arr)):
        for j in xrange(len(arr)):
            if arr[i] + arr[j] == 0 and i != j:
                if i+1 + j+1 < su:
                    su = i+1 + j+1
                    tmp = str(i+1) + ' ' + str(j+1)
    return tmp if tmp else -1
    
def main():
    k, n, arr = readdata('rosalind_2sum (3).txt')
    tmp = ''
    with open('res.txt', 'w') as f:
        for i in arr:
            tmp += str(tsum(i)) + '\n'
        f.write(tmp)
        print tmp


main()
#print readdata('test.txt')