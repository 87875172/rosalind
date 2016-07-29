def readdata(location):
    edges = []
    with open(location) as f:
        n, e = map(int,f.readline().split())
        #print n, e
        for i in f:
            edges.append(map(int,i.split()))
        #print edges
    return n, edges

def DFS(n, edges):
    nodes = range(1,n+1)
    visited_all = []

    connected = []
    for j in nodes:
        if j not in visited_all:
            stack = [j]
            visited_tmp = []
            while stack:
                tmp = stack.pop(0)
                visited_tmp.append(tmp)
                if tmp not in visited_all:
                    visited_all.append(tmp)
                for i in edges:
                    if tmp in i and tmp == i[0] and i[1] not in visited_all:
                        stack.insert(0, i[1])
                        visited_all.append(i[1])
                    elif tmp in i and tmp == i[1] and i[0] not in visited_all:
                        stack.insert(0, i[0])
                        visited_all.append(i[0])
            if visited_tmp:
                connected.append(visited_tmp)
                
    return connected, len(connected)

def main():
    n,e = readdata('rosalind_cc.txt')
    a,b = DFS(n, e)
    print a
    print b

main()