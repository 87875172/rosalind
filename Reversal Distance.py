# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 10:25:28 2016

@author: admin
"""

def readdata(location):
    tmp = []
    with open(location) as f:
        for i in f:     
            if i != '\n':
                tmp.append(map(int, i[:-1].split()))
    return tmp

def reversalble(array1, array2):
    for i in range(len(array1)):
        for j in range(len(array2)):
            #print array1[i], array2[j], array1[j], array2[i]
            if array1[i] == array2[j] and array1[j] == array2[i] and i != j:
                #print i,j                
                return (True, i, j)
    return (False, i, j)

def reversals(array):
    res = ''
    for i in range(len(array)/2):
        #print array[i*2], array[i*2 + 1]
        a = reversal_distance(array[i*2], array[i*2 + 1])
        res += str(a) + ' '
    return res



def reversal_distance(array1, array2, ans = 0):
    bo, ind1, ind2 = reversalble(array1, array2)
      
    if bo:
        ans += 1
        array1[ind1], array1[ind2] = array1[ind2], array1[ind1]
        return reversal_distance(array1, array2, ans)        
        
    return ans
        

def main():
    a = readdata('rosalind_rear.txt')
    print a
    print reversals(a)

main()