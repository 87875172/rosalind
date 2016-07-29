# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:43:53 2016

@author: admin
"""

def read_data(location):
    with open(location) as f:
        seq = f.readline()[:-1]
        k = int(f.readline()[:-1])
    return seq, k

def MF_kmer(seq, k):
    d = {}
    l = 0
    for i in range(len(seq) - k):
        if seq[i: i + k] in d:
            d[seq[i:i+k]] += 1
            if l < d[seq[i:i+k]]:
                l = d[seq[i:i+k]]
        else:
            d[seq[i:i+k]] = 1
    #print d
    #print l
    res = []
    for i in d:
        if d[i] == l:
            res.append(i)
    return res

def main():
    a = read_data('rosalind_ba1b.txt')
    
    b = MF_kmer(*a)
    #print b
    res = ''
    for i in b:
        res += i + ' '
    return res

print main()
        
        
        