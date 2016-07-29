# -*- coding: utf-8 -*-
"""
Created on Sat Jul 02 15:21:10 2016

@author: admin
"""


from numpy import zeros
from read_fasta import read_fasta as rf

def longest_commom_subsequence(seq1, seq2):
    m = zeros((len(seq1)+1, len(seq2)+1))
    
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                m[i+1][j+1] = m[i][j] + 1
            else:
                m[i+1][j+1] = max(m[i+1][j], m[i][j+1])
    #print m
    
    res = ''
    a,b = len(seq1), len(seq2)
    while a*b != 0:
        if m[a][b] == m[a-1][b]:
            a -= 1
        elif m[a][b] == m[a][b-1]:
            b -= 1
        else:
            res = seq1[a-1] + res
            a -= 1
            b -= 1
    
    return res

def main():
    a = rf('rosalind_lcsq.txt')[1]
    #print a
    print longest_commom_subsequence(a[0], a[1])
    
main()
