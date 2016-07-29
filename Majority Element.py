def readdata(location):
    with open(location) as f:
        temp = []
        for i in f:
            temp.append(i.split())
        res = []
        for i in xrange(int(temp[0][0])):
            a = []
            for j in temp[1:][i]:
                a.append(int(j))
            res.append(a)
    return int(temp[0][0]), int(temp[0][1]), res

def maj(arr):
    d = {}
    for i in arr:
        d[i] = 0
    for j in arr:
        d[j] += 1
    for k in d:
        if d[k] > len(arr)/2:
            return k
    return -1

'''def majority_element(a):
    # Initialize the candidate element and count.
    candidate, count = a[0], 0
    # Run through the list, updating the count and changing candidates as necessary.
    for element in a:
        count += [-1, 1][element == candidate]
        print count
        if count == 0:
            candidate, count = element, 1

    # Check if the candidate is indeed the majority element, returning the appropriate result.
    return [-1, candidate][a.count(candidate) > len(a)/2]
'''

def main():
    k,n,arr = readdata('rosalind_maj.txt')
    res = ''
    for i in arr:
        res += str(maj(i)) + ' '
    print res

main()