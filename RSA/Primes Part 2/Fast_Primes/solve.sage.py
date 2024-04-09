

# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_65537 = Integer(65537); _sage_const_1 = Integer(1); _sage_const_0p1 = RealNumber('0.1'); _sage_const_2 = Integer(2); _sage_const_0p5 = RealNumber('0.5'); _sage_const_0 = Integer(0); _sage_const_960 = Integer(960); _sage_const_0x1b3e6c9433a7735fa5fc479ffe4027e13bea = Integer(0x1b3e6c9433a7735fa5fc479ffe4027e13bea); _sage_const_5 = Integer(5); _sage_const_992 = Integer(992); _sage_const_1952 = Integer(1952); _sage_const_0x24683144f41188c2b1d6a217f81f12888e4e6513c43f3f60e72af8bd9728807483425d1e = Integer(0x24683144f41188c2b1d6a217f81f12888e4e6513c43f3f60e72af8bd9728807483425d1e); _sage_const_4 = Integer(4); _sage_const_1984 = Integer(1984); _sage_const_3936 = Integer(3936); _sage_const_0x16928dc3e47b44daf289a60e80e1fc6bd7648d7ef60d1890f3e0a9455efe0abdb7a748131413cebd2e36a76a355c1b664be462e115ac330f9c13344f8f3d1034a02c23396e6 = Integer(0x16928dc3e47b44daf289a60e80e1fc6bd7648d7ef60d1890f3e0a9455efe0abdb7a748131413cebd2e36a76a355c1b664be462e115ac330f9c13344f8f3d1034a02c23396e6); _sage_const_7 = Integer(7); _sage_const_3968 = Integer(3968); _sage_const_4096 = Integer(4096); _sage_const_10000 = Integer(10000); _sage_const_16 = Integer(16); _sage_const_40 = Integer(40)
import math
from sage.all import *
from sympy.ntheory import discrete_log as discrete_log_lmao



from sage.all import *

def solve(M, n, a, m):
    # I need to import it in the function otherwise multiprocessing doesn't find it in its context
    from sage_functions import coppersmith_howgrave_univariate

    base = int(_sage_const_65537 )
    # the known part of p: 65537^a * M^-1 (mod N)
    known = int(pow(base, a, M) * inverse_mod(M, n))
    # Create the polynom f(x)
    F = PolynomialRing(Zmod(n), implementation='NTL', names=('x',))
    (x,) = F._first_ngens(_sage_const_1 )
    pol = x + known
    beta = _sage_const_0p1 
    t = m+_sage_const_1 
    # Upper bound for the small root x0
    XX = floor(_sage_const_2  * n**_sage_const_0p5  / M)
    # Find a small root (x0 = k) using Coppersmith's algorithm
    roots = coppersmith_howgrave_univariate(pol, n, beta, m, t, XX)
    # There will be no roots for an incorrect guess of a.
    for k in roots:
        # reconstruct p from the recovered k
        p = int(k*M + pow(base, a, M))
        if n%p == _sage_const_0 :
            return p, n//p

def roca(n):

    keySize = n.bit_length()

    if keySize <= _sage_const_960 :
        M_prime = _sage_const_0x1b3e6c9433a7735fa5fc479ffe4027e13bea 
        m = _sage_const_5 

    elif _sage_const_992  <= keySize <= _sage_const_1952 :
        M_prime = _sage_const_0x24683144f41188c2b1d6a217f81f12888e4e6513c43f3f60e72af8bd9728807483425d1e 
        m = _sage_const_4 
        print("Have you several days/months to spend on this ?")

    elif _sage_const_1984  <= keySize <= _sage_const_3936 :
        M_prime = _sage_const_0x16928dc3e47b44daf289a60e80e1fc6bd7648d7ef60d1890f3e0a9455efe0abdb7a748131413cebd2e36a76a355c1b664be462e115ac330f9c13344f8f3d1034a02c23396e6 
        m = _sage_const_7 
        print("You'll change computer before this scripts ends...")

    elif _sage_const_3968  <= keySize <= _sage_const_4096 :
        print("Just no.")
        return None

    else:
        print("Invalid key size: {}".format(keySize))
        return None

    a3 = Zmod(M_prime)(n).log(_sage_const_65537 )
    order = Zmod(M_prime)(_sage_const_65537 ).multiplicative_order()
    inf = a3 // _sage_const_2 
    sup = (a3 + order) // _sage_const_2 

    # Search 10 000 values at a time, using multiprocess
    # too big chunks is slower, too small chunks also
    chunk_size = _sage_const_10000 
    for inf_a in range(inf, sup, chunk_size):
        # create an array with the parameter for the solve function
        inputs = [((M_prime, n, a, m), {}) for a in range(inf_a, inf_a+chunk_size)]
        # the sage builtin multiprocessing stuff
        from sage.parallel.multiprocessing_sage import parallel_iter
        from multiprocessing import cpu_count

        for k, val in parallel_iter(cpu_count(), solve, inputs):
            if val:
                p = val[_sage_const_0 ]
                q = val[_sage_const_1 ]
                print("found factorization:\np={}\nq={}".format(p, q))
                return val


primes=[]
def sieve(maximum=_sage_const_10000 ):
    # In general Sieve of Sundaram, produces primes smaller
    # than (2*x + 2) for a number given number x. Since
    # we want primes smaller than maximum, we reduce maximum to half
    # This array is used to separate numbers of the form
    # i+j+2ij from others where 1 <= i <= j
    marked = [False]*(int(maximum/_sage_const_2 )+_sage_const_1 )

    # Main logic of Sundaram. Mark all numbers which
    # do not generate prime number by doing 2*i+1
    for i in range(_sage_const_1 , int((math.sqrt(maximum)-_sage_const_1 )/_sage_const_2 )+_sage_const_1 ):
        for j in range(((i*(i+_sage_const_1 )) << _sage_const_1 ), (int(maximum/_sage_const_2 )+_sage_const_1 ), (_sage_const_2 *i+_sage_const_1 )):
            marked[j] = True

    # Since 2 is a prime number
    primes.append(_sage_const_2 )

    # Print other primes. Remaining primes are of the
    # form 2*i + 1 such that marked[i] is false.
    for i in range(_sage_const_1 , int(maximum/_sage_const_2 )):
        if (marked[i] == False):
            primes.append(_sage_const_2 *i + _sage_const_1 )


def get_primorial(n):
    result = _sage_const_1 
    for i in range(n):
        result = result * primes[i]
    return result


sieve()
n=int("4CA21EDE37E3D6A63BCEE5F9120D0989F0143AAE915302F346E8ABBB840A72FB56D1487528CA75195B7832628389092C4E893FA4A6C9B0114266E805B12DC08D",_sage_const_16 )
print(n)
e=_sage_const_65537 
print(primes)
M=get_primorial(_sage_const_40 )
print(M)


print(roca(n))

"""
x=discrete_log_lmao(M,n,e)
print(n)
print(x)
print(pow(e,x,M))
print(n%M)

#print(solve(M, n, x, 5, 6, 0.5))
#print(solve(M, n, x, 5))
#print(roca(n))
"""


