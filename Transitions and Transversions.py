from read_fasta import read_fasta

def tt_ratio(s1, s2):
    transition = 0.0
    transversion = 0.0
    for i in xrange(len(s1)):
        if s1[i] != s2[i]:
            if s1[i] in ['A', 'G'] and s2[i] in ['A', 'G'] or s1[i] in ['C', 'T'] and s2[i] in ['C', 'T']:
                transition += 1
            else:
                transversion += 1
    return transition/transversion

def main():
    a,b = read_fasta('rosalind_tran.txt')
    print tt_ratio(b[0], b[1])

main()