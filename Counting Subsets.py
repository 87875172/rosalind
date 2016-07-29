from math import factorial as fact

def Enum(x):
    
    res = 1
    
    for i in xrange(1,x+1):
        res += fact(x)/(fact(x-i)*fact(i))
    
    
    return res % 1000000

def Enum2(x):
    return 2**x % 1000000

#print Enum(877)
print Enum2(877)