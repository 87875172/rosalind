# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:00:08 2016

@author: admin
"""
from math import factorial as fact

def readdata(location):
    with open(location) as f:
        a = map(int, f.readline()[:-1].split())
        return a[0], a[1]

def combs(n, m):
    temp = 0
    for k in range(m, n+1):
        temp += fact(n)/(fact(k)*fact(n-k))
    return temp % 1000000

def main():
    a = readdata('rosalind_aspc.txt')
    print a
    print combs(*a)

main()