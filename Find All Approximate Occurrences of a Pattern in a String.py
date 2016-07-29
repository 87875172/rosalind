# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:28:57 2016

@author: admin
"""

def read_data(location):
    with open(location) as f:
        pattern = f.readline()[:-1]
        seq = f.readline()[:-1]
        k = int(f.readline()[:-1])
    return pattern, seq, k

def hamming_distance(seq1, seq2):
    res = 0    
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            res += 1
    return res

def approx_pat(pat, seq, k):
    res = ''
    l = len(pat)
    for i in range(len(seq)-l):
        if hamming_distance(pat, seq[i:i+l]) <= k:
            res += str(i) + ' '
    return res

def main():
    a = read_data('rosalind_ba1h.txt')
    b = approx_pat(*a)
    return b

print main()
    