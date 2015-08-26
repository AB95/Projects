

def fibonacci(n):
    fib = []
    a, b = 0, 1
    for i in xrange(n):
        fib.append(a)
        a, b = b, a+b

    return fib