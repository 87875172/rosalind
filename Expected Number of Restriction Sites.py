# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 17:33:36 2016

@author: admin
"""

from math import factorial as fact

def readdata(location):
    with open(location) as f:
        n = int(f.readline()[:-1])
        s = f.readline()[:-1]
        gc_arr = map(float, f.readline()[:-1].split())
    return n, s, gc_arr

def RS_occur(n, s, gc_arr):
    l = len(s)
    res = []
    for i in gc_arr:
        p = 1
        for j in s:
            if j in 'AT':
                p *= (1-i)/2.0
            elif j in 'GC':
                p *= i/2.0
        
        p *= n-l+1
        res.append(round(p,3))
    return res

def main():
    a = readdata('rosalind_eval.txt')
    #print a
    b = RS_occur(*a)
    res = ''
    for i in b:
        res += str(i) + ' '
    print res

main()