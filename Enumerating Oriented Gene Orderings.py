from itertools import permutations, product

def signed_perm(n):
    arr = range(1,n+1)+range(-n,0)
    #print arr
    tmp = []
    for i in permutations(arr, n):
        flag = 0
        #print 'i = ' + str(i)
        for j in i:
            #print 'j = ' + str(j)
            if -j in i or i in tmp:
                #print 'break j i ' + str(j) + str(i)
                flag = 1
                break
        if flag == 0:
            #print 'no break j i ' + str(j) + str(i)
            tmp.append(i)
    #print tmp
    res = ''
    for j in tmp:
        for k in j:
            res += str(k) + ' '
        res += '\n'
        
    with open('res.txt','w') as f:
        f.write(str(len(tmp)) + '\n' + res[:-1])
    
    print str(len(tmp)) + '\n' + res[:-1]

#from itertools import permutations, product
# another solution
def signedPermutations6(n):
    for perm in permutations(xrange(1, n + 1)):
        for signed_perm in product(*[(-element, element) for element in perm]):
            yield signed_perm


signed_perm(5)
#for i in signedPermutations6(5):
    #print i