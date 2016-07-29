# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:13:04 2016

@author: admin
"""
from itertools import product

def read_data(location):
    with open(location) as f:
        seq = f.readline()[:-1]
        k = int(f.readline()[:-1])
    return seq, k

def count_occur(seq, pat):
    res = 0
    for i in range(len(seq)-len(pat)+1):
        if pat == seq[i:i+len(pat)]:
            res += 1
    return res

def freq_array(seq, k):
    product(*(('ATCG '*k).split()))
    a = product(*(('ACGT '*k).split()))
    res = []
    for i in a:
        i = ''.join(i)
        #print i        
        res.append(count_occur(seq, i))
    return res

def main():
    a = read_data('rosalind_ba1k.txt')
    #print a
    #print count_occur('aaaaaa', 'aa')
    b = freq_array(*a)
    res = ''
    for i in b:
        res += str(i) + ' '
    return res

print main()