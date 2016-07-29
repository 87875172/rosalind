# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 10:24:56 2016

@author: admin
"""

def readdata(location):
    with open(location) as f:
        m = float(f.readline()[:-1])
        ions = []
        for i in f:
            ions.append(float(i[:-1]))
    return m, ions
    
def protein_mass():
    with open ('proteinmass.txt') as mass:
        d = {}
        for i in mass:
            t = i.split()
            d[t[0]] = float(t[1])
    return d

def infer_peptide(current, remain, d):
    
    for i in remain:
        for j in d:
            if abs(d[j] - (i-current)) < 0.001:
                #print d[j], i, current
                return j
    return -1
    
def all_seq(ions, d):
    n = (len(ions)-2)/2
    
    res = ''
    current = ions[0]
    remain = ions[1:]
    
    while len(res) < n:
        temp = infer_peptide(current, remain, d)
        if temp == -1:
            return res
        else:
            res += temp
            current += d[temp]
            #print str(remain) + 'before'
            remain = filter(lambda x: x-current > 0, remain)
            #print str(remain) + 'after'
    return res
            
    


def main():
    m, ions = readdata('rosalind_full.txt')
    d = protein_mass()
    #print m, ions
    #print d
    res = all_seq(ions, d)
    print res
    

main()