
def openfasta(a):
    se = []
    temp = ''
    with open(a) as test:
        for i in test:
            if i[0] != '>':
                temp += i.replace('\n','')
            else:
                se.append(temp)
                temp = ''
        se.append(temp)
    return se[1:]

a = openfasta('rosalind_cons.txt')

def profile(fasta):
    res = ['', '', '', '']
    
    n = {'0': 0, '1': 0, '2': 0, '3': 0}
    
    for i in xrange(len(fasta[0])):
        for j in fasta:
            if j[i] == 'A':
                n['0'] += 1
            if j[i] == 'C':
                n['1'] += 1
            if j[i] == 'G':
                n['2'] += 1
            if j[i] == 'T':
                n['3'] += 1

        for k in xrange(4):
            res[k] += str(n[str(k)])
        n = {'0': 0, '1': 0, '2': 0, '3': 0}
    
    
    return res
    
b = profile(a)

def consensus(profile):
    string = ''
    
    for i in xrange(len(profile[0])):
        msf = 0
        res = 'A'
        for j in xrange(4):
            #print profile[j][i]
            if profile[j][i] > msf:
                #print profile[j][i]
                msf = profile[j][i]
                if j == 0:
                    res = 'A'
                if j == 1:
                    res = 'C'
                if j == 2:
                    res = 'G'
                if j == 3:
                    res = 'T'
        string += res
    return string


def final():
    print consensus(b)
    temp = ['A: ', 'C: ', 'G: ', 'T: ']
    for i in xrange(len(b[0])):
        for j in xrange(4):
            temp[j] += b[j][i] + ' '
    for k in temp:
        print k
    

final()
