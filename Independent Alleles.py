'''
Binomial distribution
Pr(AaBb) in any generation is 1/4

Sigma(n=N, 2**k) Combinatorial(2**k, n) (1/4)**n * (3/4)**(2**k-n)
'''

import math

def IA(k, N):
    p = 1.0/4
    q = 3.0/4
    res = 0
    for i in xrange(N, 2**k+1):
        res += math.factorial(2**k)/(math.factorial(2**k-i)*math.factorial(i)) * p**i * q**(2**k-i)
    return res

print IA(5,8)