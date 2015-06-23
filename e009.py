def find_triple(n):
    for c in xrange(n):
        for b in xrange(c):
            for a in xrange(b):
                if a+b+c == n and a**2+b**2 == c**2:
                    return a*b*c


def find_triple_2(n):
    for a in range(1,n):
        for b in range(a, n-a):
            if ((a**2+b**2)**0.5) == n-a-b:
                return a*b*(n-a-b)


if __name__ == "__main__":
    from time import time

    start = time()
    print find_triple(1000)
    print "3 loop time: {}".format(time() - start)

    start = time()
    print find_triple_2(1000)
    print "2 loop time: {}".format(time() - start)

    start = time()
    print [a*b*(1000-a-b) for a in range(1,1000) for b in range(a,1000-a) if ((a**2+b**2)**0.5)==1000-a-b][0]
    print "One-liner time: {}".format(time() - start)
