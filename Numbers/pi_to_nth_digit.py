from __future__ import division
from decimal import Decimal, getcontext


# Currently accurate to 16 decimal places
def pi_to_nth_digit(n):
    getcontext().prec = 28
    pi = Decimal(0)
    for k in xrange(n):
        pi += Decimal((16**-k)*((4/(8*k+1)) - (2/(8*k+4)) - (1/(8*k+5)) - (1/(8*k+6))))

    if n == 1:
        return str(pi)[0]
    else:
        return str(pi)[:n+1]