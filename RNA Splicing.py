

def open_fasta(location):
    sequence = []
    name = []
    temp = ''
    with open(location) as fasta:
        for i in fasta:
            if i[0] == '>':
                name.append(i[:-1])
                sequence.append(temp)
                temp = ''
            elif i[0] != '>':
                temp += i.replace('\n','')
    sequence.append(temp)
    return sequence[1:]

def delete_introns(s):
    l = len(s)
    res = s[0]
    for i in xrange(1,l):
        res = res.replace(s[i],'-')
        #print 's[i] ' + s[i]
        #print 'res ' + res
    return res.replace('-','')

def DNA_to_RNA(s):
    temp = ''
    for i in s:
        if i == 'T':
            temp += 'U'
        else:
            temp += i
    return temp

#mRNA = DNA_to_RNA(b)

def DNA_to_rcRNA(s):
    temp = ''
    for i in s:
        if i == 'A':
            temp += 'U'
        if i == 'T':
            temp += 'A'
        if i == 'C':
            temp += 'G'
        if i == 'G':
            temp += 'C'
    return temp[::-1]

#rcRNA = DNA_to_rcRNA(b)

def ORF(s, n):
    c = codon('codon.txt')
    res = []
    temp = ''
    
    while n < len(s):
        if s[n:n+3] == 'AUG':
            for j in xrange(n, len(s), 3):
                if s[j:j+3] not in ['UAG','UGA','UAA'] and len(s[j:j+3]) == 3:
                    temp += c[s[j:j+3]]
                else:
                    res.append(temp)
                    temp = ''
                    n = j
                    break
        n += 3
    return res

def codon(location):
    c = {}
    temp = ''
    with open(location) as cod:
        for i in cod:
            line = i.split()
            for j in xrange(len(line)):
                #print j
                if len(line[j]) == 3:
                    temp = line[j]
                else:
                    c[temp] = line[j]
    return c

def final(s):
    a = DNA_to_RNA(s)
    #print a
    b = DNA_to_rcRNA(s)
    #print b
    res = []
    print ORF(a,0) 
    #print codon('codon.txt')
    for i in xrange(3):
        #print res
        for j in ORF(a,i):
            if j != []:
                res.append(j)
        for j in ORF(b,i):
            if j != []:
                res.append(j)
    c = list(set(res))
    
    #for k in c:
        #print k
        
a = open_fasta('rosalind_splc.txt')
#print a
b = delete_introns(a)
#print b
final(b)

#print ORF('AUGGUCUACAUAGCUGACAAACAGCACGUAGCAUCUCGAGAGGCAUAUGGUCACAUGUUCAAAGUUUGCGCCUAG', 0)