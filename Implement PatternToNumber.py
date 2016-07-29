# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:38:32 2016

@author: admin
"""

#A C G T
#0 1 2 3

def read_data(location):
    with open(location) as f:
        seq = f.readline()[:-1]
    return seq

def pat_to_num(seq):
    d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    res = 0
    l = 0
    while l < len(seq):
        l += 1
        res += d[seq[l-1]]*(4**(len(seq)-l))
    return res
        

def main():
    a = read_data('rosalind_ba1l.txt')
    #print a
    return pat_to_num(a)

print main()