# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 14:55:40 2016

@author: admin
"""

def read_data(location):
    with open(location) as f:
        seq = f.readline()[:-1]
    return seq

def min_skew(seq):
    skew = 0
    s_arr = []
    res = ''
    for i in range(len(seq)):
        s_arr.append(skew)
        if seq[i] == 'C':
            skew -= 1        
        elif seq[i] == 'G':
            skew += 1
    m = min(s_arr)
    for j, k in enumerate(s_arr):
        if k == m:
            res += str(j) + ' '
    
    return res

def main():
    a = read_data('rosalind_ba1f.txt')
    b = min_skew(a)
    return b

print main()