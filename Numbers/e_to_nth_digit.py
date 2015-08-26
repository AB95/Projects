from __future__ import division
from math import factorial
from decimal import Decimal, getcontext


# Accurate up to 16 decimal places
# Factor of 4 found empirically
def e_to_nth_digit(n):
    getcontext().prec = 28
    e = Decimal(0)
    for k in xrange(n+4):
        e += Decimal(1/factorial(k))

    if n == 1:
        return str(e)[0]
    else:
        return str(e)[:n+1]