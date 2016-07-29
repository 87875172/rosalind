# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 09:56:02 2016

@author: admin
"""

def readdata(location):
    with open(location) as f:
        n = int(f.readline()[:-1])
        A = f.readline()[:-1].strip('{}')
        B = f.readline()[:-1].strip('{}')
    
    A = A.replace(',','')   
    A = map(int, A.split())
    
    B = B.replace(',', '')
    B = map(int, B.split())    
    
    return n, A, B

def sets(n, A, B):
    a = set(A)
    b = set(B)
    c = set(range(1, n + 1))
    
    return (a|b, a&b, a-b, b-a, c-a, c-b)


def main():
    a = readdata('rosalind_seto.txt')
    #print a
    with open('res.txt', 'w') as f:
        for i in sets(*a):
            print '{' + str(list(i))[1:-1] + '}'
            f.write('{' + str(list(i))[1:-1] + '}\n')
        

main()