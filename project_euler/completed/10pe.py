#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1
        
def count_primes(x):
    
    xx = [p for i, p in zip(range(x),gen_primes())]
    
    return sum(xx)
zz = count_primes(2000001)
print(zz)
