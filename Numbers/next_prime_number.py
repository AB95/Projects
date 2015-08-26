

def prime_generator():
    yield 2
    i = 3
    while True:
        if is_prime(i):
            yield i
        i += 2


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True

    if not n % 2 or not n % 3:
        return False

    i = 5
    d = 2
    sqrt = int(n ** 0.5) + 1
    while i <= sqrt:
        if not n % i:
            return False
        i += d
        d = 6 - d
    return True

primes = prime_generator()

for _ in xrange(10):
    print primes.next()