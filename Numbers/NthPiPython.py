from __future__ import division
from decimal import Decimal, getcontext

#reference: https://www.math.hmc.edu/funfacts/ffiles/20010.5.shtml

digits = int(raw_input("Enter how many digits of pi you'd like to go to. Maximum is 1000.\n"))
while digits < 0 or digits > 1000:
    print "That number is too big"
    digits = int(raw_input("Enter how many digits of pi you'd like to go to. Maximum is 1000.\n"))

getcontext().prec = digits
pi = Decimal(0)

for k in xrange(digits+1):
    pi += Decimal((16**(-k))*((4/(8*k+1))-(2/(8*k+4))-(1/(8*k+5))-(1/(8*k+6))))

print str(pi)[:digits+1]
