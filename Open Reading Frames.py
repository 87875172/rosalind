s = 'ATAACGATCAGACAGCGACAAGCATAATAAATTTTAGATCATCAACCTAGCTACCATAAGGCGTGACTATGTAACTGAACGGTGACCCATAGTAAAAGCGTGTTGTCCCATCTTTCTGCTGCCTACCTCAGATTCCAAACATAGTTCCTTAGTTCCCCCGTGGCTGATAGGTACGCTAGCCCGGTTAGCGCTTCAAGTGCGCCGGAAACACGTCTCTAGCCCAGCGCTGAGTCTGTTAAGGCTTCAGAGTTCCGTTAACTTGTGGAATACCGTAGTAAATGATGGGCCGCTACATACCACTGGCAGATTCTCAGCATATAGACGGATCAAACTAATGGAGCCACGTATGTTTTCGGGTCACATGAGGATGAATTATGGAATTTACGCTATTTCTCGGCTGATTGAGCTATTAGTCATACCCCGATCACACAGGCGTCCCTACACGTCTTCCTGAGTGATGGCCCGCTCAAGTCCAATGGGCCGAAACTTAGGGTAGCTACCCTAAGTTTCGGCCCATCCACCATTCGTGGACGTCTGCGGTCTCAACAGGTAATTGGTCAATTGGATGAGTGAAGTGTCCTAAAGACCGTGGCCCGTGGAGGTTCAGCGTCCCGTGGCATAACTGCGTTCCCTATTCAGGTTGTTATCTGATGGGCCTGAGATTACTATGAATAGAACTTCGCTGCGTAGAATTGTTCATGTGGGAACATACGACATTTTGTCCCCCGTTATCTTGTGGTAGCAAGTACAATTAACGTCTGGTTATGCCTTTATGCCCCGCCAAACGCGTGCGATACGGGTTGTGATCAAACCTTATCGGTGGGTTGGGCATCCTCACTCTCCAGTCGTCGCCCTCCGTTTGGGTCCGCCGGCTGTAAACGACTTTCACACCAGATGATGAGTCATGGAGCAAGCGCAGGAACAAACAAGGAATCCTTGTCCTGTCGAGTAGGGAATTAACTGTCCCAGAACAGGTACTAGGCCCAGCCGAA'

def RNA(s):
    temp = ''
    for i in s:
        if i == 'T':
            temp += 'U'
        else:
            temp += i
    return temp



def rcRNA(s):
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


def ORF(s, n):
    c = codon('codon.txt')
    res = []
    temp = ''
    

    for i in xrange(n, len(s), 3):
        if s[i:i+3] == 'AUG':
            for j in xrange(i, len(s), 3):
                if s[j:j+3] not in ['UAG','UGA','UAA']:
                    temp += c[s[j:j+3]]
                else:
                    res.append(temp)
                    temp = ''
                    break
    return res

def codon(f):
    c = {}
    temp = ''
    with open(f) as cod:
        for i in cod:
            line = i.split()
            for j in xrange(len(line)):
                #print j
                if len(line[j]) == 3:
                    temp = line[j]
                else:
                    c[temp] = line[j]
    return c

def final():
    a = RNA(s)
    b = rcRNA(s)
    res = []
    for i in xrange(3):
        for j in ORF(a,i):
            if j != []:
                res.append(j)
        for j in ORF(b,i):
            if j != []:
                res.append(j)
    c = list(set(res))
    
    for k in c:
        print k

final()