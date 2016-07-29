def partial_permutations(n, k):
    from math import factorial
    return factorial(n)/factorial(n-k) % 1000000

print partial_permutations(98, 5)