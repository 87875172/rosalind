# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 11:47:15 2016

@author: admin
"""

def read_data(location):
    with open(location) as f:
        seq = f.readline()[:-1]
        k, L, t = map(int, f.readline()[:-1].split())
    return seq, k, L, t

def find_clump(seq, k, L, t):
    res = []
    for i in range(len(seq) - L):
        
        d = {}
        #print i
        #print type(k)
        for j in range(L - k):
            if seq[i:i+L][j:j+k] not in d:
                d[seq[i:i+L][j:j+k]] = 1
            else:
                d[seq[i:i+L][j:j+k]] += 1
        #print d
        #print d['CGACA']
        for m in d:
            if d[m] == t and m not in res:
                res.append(m)
    return res
    

def main():
    a = read_data('rosalind_ba1e.txt')
    #print a
    #print len(a[0])
    b = find_clump(*a)
    res = ''
    for i in b:
        res += i + ' '
    return res
    

print main()