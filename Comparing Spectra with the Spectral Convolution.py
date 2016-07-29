# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 13:58:22 2016

@author: admin
"""

def read_data(location):
    with open(location) as f:
        S1 = map(float, f.readline().split())
        S2 = map(float, f.readline().split())
    return S1, S2

def Minkowski_difference(S1, S2):
    tmp = []
    for s1 in S1:
        for s2 in S2:
            tmp.append(round(s1-s2,5))
    
    c = 0
    num = -1.0
    for i in tmp:
        if tmp.count(i) > c:
            c = tmp.count(i)
            num = i
    return c, num



def main():
    S1, S2 = read_data('rosalind_conv.txt')
    #print S1, S2
    count, num = Minkowski_difference(S1, S2)
    print count
    print num

main()