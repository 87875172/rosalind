from math import factorial

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
    
a = open_fasta('rosalind_mmch.txt')[0]
#print a
def MM(seq):
    A = seq.count('A')
    U = seq.count('U')
    C = seq.count('C')
    G = seq.count('G')
    
    if A > U:
        MMAU = factorial(A)/factorial(A-U)
    else:
        MMAU = factorial(U)/factorial(U-A)
    if C > G:
        MMGC = factorial(C)/factorial(C-G)
    else:
        MMGC = factorial(G)/factorial(G-C)
    return MMAU*MMGC

print MM(a)
print MM('AAUGCUUC')
