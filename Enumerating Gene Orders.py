from itertools import permutations

def Enum(x, outfile):
    a = range(1,x+1)
    #print a
    with open(outfile,'w') as f:
        n = []
        for k in permutations(a):
            n.append(k)
        f.write(str(len(n)) + '\n')
        for j in permutations(a):
            b = str(j).replace(',','')
            f.write(b.strip('()') + '\n')

Enum(7, 'test.txt')