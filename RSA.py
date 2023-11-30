import random
import math
import fermat
from extended_euclid import extended_euiclid as ee

def rsa_decrypt(d, c, n):
    m = pow(c, d, n)
    str_m = str(m)  
    out = ""
    for i in range(0, len(str_m), 2):
        pair = str_m[i:i+2]
        out += chr(int(pair) + ord('a')-1)
    print(out)

rsa_decrypt(264209248715, 490405233529, 509399820229)

def rsa_get_d(e, n):
    p, q = fermat.fermat_factorization(n)
    k = (p-1)*(q-1)
    d = pow(e, -1, k)
    return d

rsa_decrypt(rsa_get_d(482333806279, 685035429137), 390008522177, 685035429137)

def rsa_lucky_prime(n, n_prime, e):
    p = ee(n, n_prime)[-1]
    q = n // p
    k = (p-1)*(q-1)
    d = pow(e, -1, k)
    return d

rsa_decrypt(rsa_lucky_prime(33014225445779628048658397734407409844770496303343715202362283, 60887715997030736240293995011807515303605202128399598272861227, 21965492946170129340427429793577060905853790070522036884939213), 17558158294187236145026049715045716230598547118322513025364758, 33014225445779628048658397734407409844770496303343715202362283)
