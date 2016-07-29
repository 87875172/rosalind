# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 04:22:07 2016

@author: admin
"""

def read_data(location):
    with open(location) as f:
        N, gc_content = map(float, f.readline().split())
        N = int(N)
        seq = f.readline()[:-1]
    return N, gc_content, seq

def cal_pro(gc_content, seq):
    #gc2 = cal_gc(seq)
    #gc_diff = len(seq) * (gc2 - gc_content)
    d = {'A': (1-gc_content)/2, 'T': (1-gc_content)/2, 'C': gc_content/2, 'G': gc_content/2}
    
    res = 1.0
    for i in seq:
        res *= d[i]
    return 1 - res
    

def main():
    N, gc_content, seq = read_data('rosalind_rstr.txt')

    res = cal_pro(gc_content, seq)
    
    print round(1 - res ** N, 3)
    

main()
