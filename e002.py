def nth_fib_rec(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return nth_fib(n-1) + nth_fib(n-2)


def fib_sum_rec(last=1, lastbutone=1, total=0):
    newnum = last + lastbutone
    if newnum > 4000000:
        return total
    if (newnum%2 == 0):
        return fib_sum_rec(newnum, last, total+newnum)
    else:
        return fib_sum_rec(newnum, last, total)


def fib_gen():
    a, b = 0, 1
    #yield a
    #yield b
    while True:
        a, b = b, a + b
        yield b


def fib_gen_sum(n):
    s, b  = 0, 0
    fib = fib_gen()
    while b <= n:
        b = fib.next()
        if b%2 == 0:
            s += b
    return s


def fib_sum(n):
    def fib(n):
        a, b = 0, 1
        while a <= n:
            a, b = b, a + b
            yield b
    return sum([i for i in fib(n) if i%2 == 0])


if __name__ == "__main__":
    from time import time

    start = time()
    print fib_sum_rec()
    print "Recursive sum time: {}".format(time() - start)

    start = time()
    print fib_gen_sum(4000000)
    print "Iterative generator sum time: {}".format(time() - start)

    start = time()
    print fib_sum(4000000)
    print "Iterative sum time: {}".format(time() - start)

