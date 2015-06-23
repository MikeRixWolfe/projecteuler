from e021 import d_sum


def non_abundant_sums(n):
    a = []
    s = 0
    for i in xrange(n):
        if i < d_sum(i):
            if i not in a:
                a.append(i)
            for x in a:
                if x+i not in a:
                    a.append(x+i)
        if i not in a:
            s += i
    return s


if __name__ == "__main__":
    from time import time

    start = time()
    #print non_abundant_sums(28123)
    print "Time: {}".format(time() - start)
