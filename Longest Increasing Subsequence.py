def readdata(location):
    with open(location) as f:
        n = f.readline()
        pi = f.readline().split()
    res = []
    for i in pi:
        res.append(int(i))
    return int(n), res

#print readdata('test.txt')

def long_incr_sub2(arr): #return length
    ind = []
    for i in arr:
        ind.append(1)
    for j in xrange(len(arr)):
        for k in xrange(len(arr)):
            if arr[j] < arr[k] and ind[j]+1 > ind[k]:
                ind[k] = ind[j]+1
    return max(ind)

def long_incr_sub3(arr):
    ind = []
    for i in arr:
        ind.append(1)

    for i in xrange(len(ind)):
        m = -1
        for j in xrange(0, i):
            if arr[i] > arr[j]:
                if m == -1 or m < ind[j] + 1:
                    m = 1 + ind[j]
        if m == -1:
            m = 1
        ind[i] = m
    #print ind
    tmp = -1
    n = -1
    for l in xrange(len(arr)):
        if tmp < ind[l]:
            tmp = ind[l]
            n = l
        
    path = str(arr[n])
    res = tmp - 1
    for i in xrange(n-1, -1, -1):
        if ind[i] == res:
            path = str(arr[i]) + ' ' + path
            res -= 1
    return tmp, path
    
def long_decr_sub(arr):
    ind = []
    for i in arr:
        ind.append(1)

    for i in xrange(len(ind)):
        m = -1
        for j in xrange(0, i):
            if arr[i] < arr[j]: # only difference '<'
                if m == -1 or m < ind[j] + 1:
                    m = 1 + ind[j]
        if m == -1:
            m = 1
        ind[i] = m
    #print ind
    tmp = -1
    n = -1
    for l in xrange(len(arr)):
        if tmp < ind[l]:
            tmp = ind[l]
            n = l
        
    path = str(arr[n])
    res = tmp - 1
    for i in xrange(n-1, -1, -1):
        if ind[i] == res:
            path = str(arr[i]) + ' ' + path
            res -= 1
    return tmp, path
    


# Very fast solution

def lgis( X, compare_func ):
    piles = []

    for i in X:
        try:
            idx = next(j for j in range(len(piles)) if compare_func(piles[j][-1][0],i))
            piles[idx].append((i,len(piles[idx-1]) if idx > 0 else -1))
        except StopIteration:
            piles.append( [(i,len(piles[-1]) if piles else -1)])

    result = []
    bp = -1
    for i in range(len(piles)-1,-1,-1):
        result.append(piles[i][bp][0])
        bp = piles[i][bp][1]-1

    return result[::-1]

#f = open( "rosalind_lgis.txt")
#f.readline()
#X = map( int, f.readline().split())



'''
# print all the longest increasing subsequences

def printLIS(lst, LIS):
  maxlen = 0
  for i in range (0, len(LIS)):
    if( LIS[i][0][0] > maxlen ):
      maxlen = LIS[i][0][0]
      
  for i in range (0, len(LIS)):
    if( LIS[i][0][0] == maxlen ):
      printLIS_h(lst, LIS, i, "")      
  
def printLIS_h(lst, LIS, index, str):
  for tuple in range ( 0, len(LIS[index]) ):
    if( LIS[index][tuple][1] == index ):
      print lst[index],str
    else:
      printLIS_h(lst, LIS, LIS[index][tuple][1], `lst[index]`+" "+str)

def find_lis(lst):
  LIS = []
  LIS.append([(1,0)])

  for i in range (1, len(lst)):
    LIS.append([])
    for j in range (0, i):
      if( lst[i] >= lst[j]):
        if( len(LIS[i]) != 0 and ( LIS[i][0][0] < (LIS[j][0][0]+1))):
          del LIS[i][:]
          
        if( len(LIS[i]) == 0 or LIS[i][0][0] == (LIS[j][0][0]+1) ):
          num = LIS[j][0][0] + 1
          LIS[i].append( (num,j) )

      elif ( len(LIS[i]) == 0 ):
        LIS[i].append((1,i))

  printLIS(lst, LIS)


#if __name__ == "__main__":
#  lst = [int(x) for x in raw_input().split()]
#  find_lis(lst)
'''

def main():
    n, pi = readdata('rosalind_lgis.txt')
    #print pi
    #a = long_incr_sub3(pi)
    #b = long_decr_sub(pi)
    #print find_lis(pi)
    print lgis(pi, lambda a,b: a > b)
    print lgis(pi, lambda a,b: a < b)
    #print a[1]
    #print b[1]
    
    
main()