from e021 import d_sum

abundants = []

def divisors(n):
    yield 1
    for i in xrange(2, long(n**.5)+1):
        if n % i == 0:
            yield i
            if i != n/i:
                yield n/i


def is_abundant(n):
    return sum(divisors(n)) > n


def is_abundant_sum(n):
    abundants_set = set(abundants)
    for i in abundants:
        if i > n:
            return False
        if (n - i) in abundants_set:
            return True
    return False

def non_abundant_sums(n):
    global abundants
    abundants = [x for x in xrange(1, n+1) if is_abundant(x)]

    for i in xrange(1, n+1):
        if not is_abundant_sum(i):
            yield i


if __name__ == "__main__":
    from time import time

    start = time()
    print sum(non_abundant_sums(28123))
    print "Time: {}".format(time() - start)
