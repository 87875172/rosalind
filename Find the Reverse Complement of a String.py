# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 17:06:21 2016

@author: admin
"""
def readdata(location):
    with open(location) as f:
        s = f.readline()
    return s[:-1]

def reverse_complement(s):
    d = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    res = ''
    for i in s:
        res += d[i]
    return res[::-1]

def main():
    a = readdata('rosalind_ba1c.txt')
    print reverse_complement(a)
    
main()
