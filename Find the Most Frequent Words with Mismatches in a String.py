# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:39:19 2016

@author: admin
"""

from itertools import product

def read_data(location):
    with open(location) as f:
        seq = f.readline()[:-1]
        k, d = map(int, f.readline()[:-1].split())
    return seq, k, d

def hamming_distance(seq1, seq2):
    res = 0    
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            res += 1
    return res

def kmers(k):
    return product(*(('ATCG '*k).split()))

def max_value(dic):
    m = -1
    for i in dic:
        if dic[i] > m:
            m = dic[i]
    if m == -1:
        return 0
    else:
        return m

def words_with_mismatch(seq, k, d):
    di = {}
    res = []
    for i in kmers(k):
        di[''.join(i)] = 0
    
    for j in di:
        di[j] = 0
        for l in range(len(seq) - k):
            if hamming_distance(seq[l:l+k], j) <= d:
                di[j] += 1
        ma = max_value(di)
        tmp = []
        if ma != -1:
            for n in di:
                if di[n] == ma and n not in tmp:
                    tmp.append(n)
        if [tmp, ma] not in res:
            res.append([tmp, ma])
    return res[-1][0]
        

def main():
    res = ''
    a = read_data('rosalind_ba1i.txt')
    b = words_with_mismatch(*a)
    for i in b:
        res += i + ' '
    return res

print main()