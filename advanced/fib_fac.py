#-*- coding: utf-8 -*-


def factorial(n):
    """Return the factorial of n"""
    if n < 2:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Return the nth fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_fac(x=30, y=900):
    fib = fibonacci(x)
    fac = factorial(y)
    print "fibonacci({}):".format(x), fib
    print "factorial({}):".format(y), fac


if __name__ == "__main__":
    def opc1():
        fruits = tuple(str(i) for i in xrange(100))
        out = ''
        for fruit in fruits:
            out += fruit +':'
        return out
    
    def opc2():
        format_str = '%s:' * 100
        fruits = tuple(str(i) for i in xrange(100))
        out = format_str % fruits
        return out
    
    def opc3():
        format_str = '{}:' * 100
        fruits = tuple(str(i) for i in xrange(100))
        out = format_str.format(*fruits)
        return out
    
    def opc4():
        fruits = tuple(str(i) for i in xrange(100))
        out = ':'.join(fruits)
        return out
    import timeit
    print timeit.timeit(stmt=opc4, number=100)
    fib_fac()
