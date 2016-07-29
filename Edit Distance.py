# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 11:29:40 2016

@author: admin
"""

from numpy import zeros
from read_fasta import read_fasta as rf

def edit_distance(seq1, seq2):
    m = zeros((len(seq1)+1, len(seq2)+1))
    
    for i in range(1, len(seq1) + 1):
        m[i][0] = i
    
    for j in range(1, len(seq2) + 1):
        m[0][j] = j
    
    
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            if seq1[i-1] == seq2[j-1]:
                m[i][j] = m[i-1][j-1]
            else:
                m[i][j] = min(m[i-1][j] + 1, m[i][j-1] + 1, m[i-1][j-1] + 1)
    
    return int(m[len(seq1), len(seq2)])


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
    seqs = rf('rosalind_edit.txt')
    a = edit_distance(seqs[1][0], seqs[1][1])
    
    print a
    

main()