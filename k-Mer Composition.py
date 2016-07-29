# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 09:47:24 2016

@author: admin
"""

from read_fasta import read_fasta as rf
from itertools import product as pro
#from collections import OrderedDict as OD


def four_mer(seq):
    d = {}
    for i in pro('ACGT','ACGT','ACGT','ACGT'):
        d[''.join(i)] = 0
    
    for i in range(len(seq)-3):
        d[seq[i:i+4]] += 1
    return d



def main():
    a = rf('rosalind_kmer.txt')[1][0]
    b = four_mer(a)
    s = sorted(b)
    tmp = ''
    
    for i in s:
        tmp += str(b[i]) + ' '
    print tmp
    #for i in b:
        #tmp.append([i, b[i]])
    #print tmp
    

main()