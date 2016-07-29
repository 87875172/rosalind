from read_fasta import read_fasta

def get_data(location):
    s, t = read_fasta(location)
    return t[0], t[1]

def sub_seq(s, t):
    res = ''
    counter = -1
    for i in t:
        for j in xrange(len(s)):
            if i == s[j] and j > counter:
                counter = j
                res += str(j+1) + ' '
                break
    return res

def main():
    s, t = get_data('rosalind_sseq.txt')
    print sub_seq(s, t)

main()