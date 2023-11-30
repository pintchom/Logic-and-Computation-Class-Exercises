import math 
import random

def fermatTest(n,ntrials):    
    for trial in range(ntrials):
        if pow(random.randint(1, n-1), n-1, n) != 1:
            return False
    return True

def fermatPrime(max, ntrials):
    n = random.randint(1, max)
    while fermatTest(n, ntrials) == False:
        n = random.randint(1, max)
    return n 

#print(fermatPrime(20000, 10))


def fermat_factorization(n):

    a = math.ceil(math.sqrt(n))
    b2 = a**2 - n

    while not math.isqrt(b2)**2 == b2:
        a += 1
        b2 = a**2 - n

    b = math.isqrt(b2)
    p = a + b
    q = a - b
    return p, q