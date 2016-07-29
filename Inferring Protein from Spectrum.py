def read_spectrum(location):
    with open(location) as temp:
        s = []
        for i in temp:
            s.append(float(i.replace('\n','')))
    s.sort()
    #print s
    with open ('proteinmass.txt') as mass:
        d = {}
        for i in mass:
            t = i.split()
            d[t[0]] = float(t[1])
    #print d
    res = ''
    
    for j in xrange(len(s)-1):
        for k in d:
            if abs(d[k] - (s[j+1] - s[j])) < 0.0001:
                res += k
                break
    #print len(res)
    #print len(s)
    return res

print read_spectrum('rosalind_spec.txt')