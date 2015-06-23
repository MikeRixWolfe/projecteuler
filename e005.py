def smallest_multiple():
    def is_divisible(n):
        for i in xrange(11, 21):
            if n%i != 0:
                return False
        return True
    i = n = 2520
    while True:
        i += n
        if is_divisible(i):
            return i


if __name__ == "__main__":
    from time import time

    start = time()
    print smallest_multiple()
    print "Time: {}".format(time() - start)

