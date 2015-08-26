

def find_prime_factors(n):
    i = 2
    factors = []
    while not n % i:
        n //= i
        factors.append(i)
    i += 1
    while i * i <= n:
        if n % i:
            i += 2
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors