def readdata(location):
    with open(location) as f:
        name = []
        se2 = []
        temp = ''
        
        for i in f:
            if i[0] == '>':
                name.append(i[1:-1])
                se2.append(temp)
                temp = '' 
                
            elif i[0] != '>':
                temp += i
        
        se2.append(temp)

        se2.pop(0)
        se = []
        
        for m in se2:
            se.append(m.replace('\n',''))
    return name, se

def superstring(arr, sup = ''):
    if sup == '':
        sup = arr.pop(0)
        return superstring(arr, sup)
    
    elif not arr:
        return sup
    
    else:
        
        for i in xrange(len(arr)):
            l = len(arr[i])
            
            for p in xrange(l/2):
                q = l - p
                
                if sup.startswith(arr[i][p:]):
                    sup = arr[i][:p] + sup
                    arr.pop(i)
                    return superstring(arr, sup)
                elif sup.endswith(arr[i][:q]):
                    sup = sup + arr[i][q:]
                    arr.pop(i)
                    return superstring(arr, sup)
    

def main():
    name, arr = readdata('rosalind_long (2).txt')
    res = superstring(arr)
    with open('res.txt','w') as f:
        f.write(res)
    print res
    
main()