def readdata(location):
    with open(location) as f:
        a = f.readline()
        res = []
        for i in f:
            temp = []
            for j in i.split():
                temp.append(int(j))
            res.append(temp)
        #print res[0][-1]
        #print res[0]
    return res[0]

def par(arr):

    counter = 0
    left_index = []
    right_index = []
    for i in xrange(len(arr)):
        if arr[i] <= arr[0] and i != 0:
            counter += 1
    arr[0], arr[counter] = arr[counter], arr[0]
    
    for j in xrange(len(arr)):
        if arr[j] > arr[counter] and j < counter:
            left_index.append(j)
        elif arr[j] < arr[counter] and j > counter:
            right_index.append(j)
    
    for k in xrange(len(left_index)):
        arr[left_index[k]], arr[right_index[k]] = arr[right_index[k]], arr[left_index[k]]
    
    '''for j in xrange(len(arr)):
        for k in xrange(len(arr)):
            if arr[j] > arr[counter] and arr[k] < arr[counter] and j < counter < k:
                arr[j], arr[k] = arr[k], arr[j]'''
    return arr

def main():
    a = readdata('rosalind_par (2).txt')
    res = ''
    for i in par(a):
        res += str(i) + ' '
    with open('res.txt','w') as f:
        f.write(res)
    print res

main()
#print par([7,2,5,6,1, 3, 9, 4, 8])
#print readdata('test.txt')