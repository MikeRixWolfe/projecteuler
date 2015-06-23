from e003 import is_prime


def sum_of_primes(n):
    s = 2
    for i in xrange(3, n, 2):
        if is_prime(i):
            s+=i
    return s


def sieve_of_erastothenes(n):
    mark = [True] * n
    mark[0] = mark[1] = False
    s = 0
    for i in xrange(n):
        if mark[i]:
            s += i
            for j in xrange(i, n, i):
                mark[j] = False
    return s


if __name__ == "__main__":
    from time import time

    #start = time()
    #print sum_of_primes(2000000)
    #print "Brute-force time: {}".format(time() - start)

    start = time()
    print sieve_of_erastothenes(2000000)
    print "Sieve of Erastothenes time: {}".format(time() - start)
