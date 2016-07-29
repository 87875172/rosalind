# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 12:38:03 2016

@author: admin
"""

def read_data(location):
    with open(location) as f:
        a = f.readline()[:-1].split()
        c= ''.join(a)
        b = int(f.readline()[:-1])
    return c,b

    
def alpha_combs(alphabet, n, acc='', res=[]):
    if n > 0:
        for c in alphabet:
            res.append(acc + c)
            alpha_combs(alphabet, n - 1, acc + c, res)
    return res

def main():
    seq, n = read_data('rosalind_lexv.txt')
    res = alpha_combs(seq, n)
    #print res
    with open('res.txt','w') as f:
        for i in res:
            f.write(i + '\n')
            #print i
main()