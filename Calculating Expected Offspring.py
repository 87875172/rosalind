'''
1. AA-AA
2. AA-Aa
3. AA-aa
4. Aa-Aa
5. Aa-aa
6. aa-aa'''

a= '19696 18212 18139 19067 16693 17199'
b = a.split()


c = []

for i in b:
    c.append(float(i))

res = c[0]*2 + c[1]*2 + c[2]*2 + c[3]*2*3.0/4 + c[4]*2*1.0/2

print res