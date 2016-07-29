from read_fasta import read_fasta

def Motif(seq):
    n = len(seq)
    res = []
    for k in xrange(1, n + 1):
        m = 0
        for j in xrange(2, k + 1):
            if seq[j-1:k] == seq[0:k-j+1] and k - j > m:
                #print seq[j-1:k-1]
                #print seq[0:k-j]
                m = k - j + 1 
                break
            elif j == k and seq[j-1] == seq[0] and m == 0:
                m = 1
                break
        res.append(m)
    
    return res

def Motif2(seq): #Wrong solution
    n = len(seq)
    tmp = [0] * n
    
    j = 0
    for k in xrange(2, n):
        while j > 0 and seq[j] != seq[k-1]:
            j = tmp[k-1]
        if seq[j] == seq[k-1]:
            j += 1
        tmp[k-1] = j
    return tmp

def kmp_preprocess(s):
    j = -1
    b = [j]

    for c in s:
        while j >= 0 and s[j] != c:
            j = b[j]
        j += 1
        b.append(j)

    return b[1:]

def main():
    name, seq = read_fasta('test.txt')    # rosalind_kmp.txt
    tmp = kmp_preprocess(seq[0])
    #print tmp
    res = ''
    for i in tmp:
            res += str(i) + ' '
    with open('res.txt','w') as f:
        f.write(res)
        
    print res

    

main()