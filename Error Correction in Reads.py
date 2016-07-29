# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 11:35:45 2016

@author: admin
"""

from read_fasta import read_fasta as rf

def reverse_comp(seq):
    d = {'A':'T','C':'G','G':'C','T':'A'}
    tmp = ''
    for i in seq:
        tmp += d[i]
    return tmp[::-1]

def count_mutat(seq1, seq2):
    res = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
           res += 1
    return res

def error_correc(arr):
    err = []
    cor = []
    #print len(arr)
    for i in range(len(arr)):
        tmp = arr[:]
        tmp.pop(i)
        if arr[i] not in tmp and reverse_comp(arr[i]) not in tmp:
            #if arr[i] not in err:
            err.append(arr[i])
        else:
            cor.append(arr[i])
    
    #print cor
    #print err
    #print len(err)
    
    res = []
    
    for i in err:
        for j in cor:
            if count_mutat(i,j) == 1:
                res.append([i,j])
                #print i + '->' + j #+ '\n'
                break
            elif count_mutat(i,reverse_comp(j)) == 1:
                res.append([i,reverse_comp(j)])
                #print i + '->' + reverse_comp(j) #+ '\n'
                break
    with open('res.txt','w') as f:
        for i in res:
            f.write(i[0] + '->' + i[1] + '\n')
    
    
def main():
    a = rf('rosalind_corr.txt')[1]
    error_correc(a)

main()