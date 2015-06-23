def sumdiv35(n):
    return sum([i for i in xrange(3, n) if (i%3 == 0 or i%5 == 0)])


if __name__ == "__main__":
    from time import time

    start = time()
    print sumdiv35(1000)
    print "Time: {}".format(time() - start)

