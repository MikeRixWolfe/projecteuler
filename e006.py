def sum_of_squares(n):
    s = 0
    for i in xrange(n+1):
        s += i**2
    return s


def square_of_sum(n):
    s = 0
    for i in xrange(n+1):
        s += i
    return s**2


if __name__ == "__main__":
    from time import time

    start = time()
    print square_of_sum(100) - sum_of_squares(100)
    print "Time: {}".format(time() - start)

