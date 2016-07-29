# -*- coding: utf-8 -*-
"""
Created on Sat Jul 02 15:45:24 2016

@author: admin
"""

#Compute the Number of Times a Pattern Appears in a Text

def pat(seq1, pattern):
    l = len(pattern)
    res = 0
    for i in range(len(seq1) - l + 1):
        if seq1[i:i+l] == pattern:
            res += 1
    return res

def readdata(location):
    with open(location) as f:
        seq = f.readline()
        pattern = f.readline()
    return seq[:-1], pattern[:-1]

def main():
    seq,p = readdata('rosalind_ba1a.txt')
    #print (seq,p)
    print pat(seq,p)

main()