def d_sum(n):
    s = 1
    for i in xrange(2, long(n**.5)+1):
        if n%i == 0:
            s += i + n/i
    return s


def amicable(n):
    s = 0
    for a in xrange(2, n, 2):
        b = d_sum(a)
        if d_sum(b) == a and a != b:
            s += a
    return s


if __name__ == "__main__":
    from time import time

    start = time()
    print amicable(10000)
    print "Time: {}".format(time() - start)
