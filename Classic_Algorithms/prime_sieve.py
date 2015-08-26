

def prime_sieve(n):
    if n > 0:
        primes = [True if i%2 else False for i in xrange(n+1)]
        primes[1] = False
        if n > 1:
            primes[2] = True
        sqrt = int(n ** 0.5) + 1
        i = 3
        while i <= sqrt:
            for j in xrange(i*i, n, i):
                primes[j] = False
            i += 1
        return [i for i, n in enumerate(primes) if n]