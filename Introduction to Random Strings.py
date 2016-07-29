from math import log

def readdate(location):
    with open(location) as f:
        s = f.readline()
        tmp = f.readline().split()
        A = []
        
        for i in tmp:
            A.append(float(i))
        
    return s[:-1], A

#print readdate('test.txt')

def cal_prob(Ak, s):
    d = {'A': (1-Ak)/2, 'T': (1-Ak)/2, 'C': Ak/2, 'G': Ak/2}
    
    res = 1.0
    for i in s:
        res *= d[i]
    return log(res, 10)

#print cal_prob(0.129, 'ACGATACAA')
def main():
    s, A = readdate('rosalind_prob.txt')
    res = ''
    for i in A:
        res += str(round(cal_prob(i, s), 3)) + ' '
    print res

main()