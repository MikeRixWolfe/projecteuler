def is_prime(n):
    for j in xrange(3, long(n**.5)+1, 2):
        if n%j == 0 or n%2 == 0:
            return False
    return True


def lpf(n):
    for i in xrange(3, long(n**.5)+1, 2):
        if n%i == 0:
            if is_prime(i):
                s = i
    return s


if __name__ == "__main__":
    from time import time

    start = time()
    print lpf(600851475143)
    print "LPF time: {}".format(time() - start)
