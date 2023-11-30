import sys
import random
import math
sys.setrecursionlimit(2500)

def extended_euiclid(n, m):
    if m == 0:
        return (1, 0, n)
    (q, r) = divmod(n, m)
    (a, b, d) = extended_euiclid(m, r)
    return (b, a-b*q , d)

#print(extended_euiclid(random.randint(100000000000**100,999999999999**100), random.randint(100000000000**100,999999999999**100)))
#print(pow(2, 10000, 10001))