# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 03:56:03 2016

@author: admin
"""

from read_fasta import read_fasta as rf

def distance_matrix(arr):
    #res = ''
    mat = []
    for i in xrange(len(arr)):
        for j in xrange(len(arr)):
            mat.append(p_distance(arr[i], arr[j]))
    return mat

def p_distance(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError
    tmp = 0.0
    for i in xrange(len(arr1)):
        if arr1[i] != arr2[i]:
            tmp += 1
    return round(tmp/len(arr1), 5)
        

def main():
    names, seqs = rf('rosalind_pdst.txt')
    #print seqs
    #print p_distance(seqs[1],seqs[2])
    tmp = distance_matrix(seqs)
    res = ''
    for i in xrange(len(tmp)):
        if i % len(seqs) == 0 and i != 0:
            res += '\n'
        res += str(tmp[i]) + ' '
    print res

main()
