# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:05:34 2016

@author: admin
"""

def read_data(location):
    with open(location) as f:
        seq1 = f.readline()[:-1]
        seq2 = f.readline()[:-1]
    return seq1, seq2

def hamming_distance(seq1, seq2):
    res = 0    
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            res += 1
    return res

def main():
    a = read_data('rosalind_ba1g.txt')
    b = hamming_distance(*a)    
    return b

print main()