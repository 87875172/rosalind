def readdata(location):
    with open(location) as f:
        a = f.readline()
        nodes = range(1, int(a.split()[0])+1)
        #e_num = int(a.split()[1])
        tmp = []
        edges = []
        for i in f:
            tmp.append(i.split())
        for j in tmp:
            a = []
            for k in j:
                a.append(int(k))
            edges.append(a)
    return nodes, edges

#print readdata('test.txt')

def adjacency_list(nodes, edges):
    tmp = []
    for i in nodes:
        tmp.append([])
        
    for j in nodes:
        #print j
        temp = []
        for k in edges:
            if j == k[0]:
                temp.append(k[1])
            if j == k[1]:
                temp.append(k[0])
        tmp[j-1] = temp
    
    return tmp

def Deg(nodes, edges):
    res = {}
    for i in nodes:
        temp = 0
        for j in edges:
            if i == j[0] and j[1] in nodes:
                temp += 1
            elif i == j[1] and j[0] in nodes:
                temp += 1
        res[i] = temp
    return res
    
def main():
    a,b = readdata('rosalind_ddeg.txt')
    c = adjacency_list(a,b)
    d = Deg(a,b)
    
    res = ''
    
    for i in c:
        tmp = 0
        for j in i:
            tmp += d[j]
        res += str(tmp) + ' '
    print res

main()