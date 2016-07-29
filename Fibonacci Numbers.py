res = {1:1, 2:1}
def fib(n):
    if n in res:
        return res[n]
    res[n] = fib(n-1) + fib(n-2)
    return fib(n-1) + fib(n-2)

def fib2(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib2(n-1) + fib2(n-2)

#print fib(222)
#print fib2(46)

def fib3(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    arr = [0, 1]
    
    for i in xrange(2, n+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr[n]

print fib3(222)