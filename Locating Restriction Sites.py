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

def is_palindrome(s):
    d = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    
    for i in xrange(len(s)):
        if d[s[i]] != s[len(s) - i - 1]:
            return False
    return len(s)

#print is_palindrome('GCATGC')

def every_palindrome(arr):
    res = []
    for i in arr:
        #print i
        for j in xrange(len(i)):
            for k in xrange(j,len(i)):
                l = is_palindrome(i[j:k+1])
                if 4 <= l <= 12:
                    res.append(str(j+1) + ' ' + str(l))
    return res


a = open_fasta('rosalind_revp.txt')
for i in every_palindrome(a):
    print i


        


