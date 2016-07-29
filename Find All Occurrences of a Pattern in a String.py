# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 16:04:23 2016

@author: admin
"""

def read_data(location):
    with open(location) as f:
        pattern = f.readline()[:-1]
        genome = f.readline()[:-1]
    return pattern, genome

def index(p, g):
    res = ''
    for i in range(len(g)-len(p)):
        if g[i:i+len(p)] == p:
            res += str(i) + ' '
    return res

def main():
    a = read_data('rosalind_ba1d.txt')
    b = index(*a)
    return b

print main()