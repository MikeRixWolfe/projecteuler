def fac(n):
    if n == 0:
        return 1
    return reduce(lambda x, y: x*y, [i for i in reversed(xrange(1, n+1))])


def nth_lex_perm_iter(r, x):
    s = ""
    for i in reversed(range(len(x))):
        # we must have a remainder
        d = r/fac(i) if r-(r/fac(i))*fac(i) != 0 else r/fac(i)-1
        _r, r = r, r-d*fac(i)
        s += str(x.pop(d))  # get dth smallest
        #print "{}={}({}!)+{}\n\t{} {}".format(_r, d, i, r, s, x)
    return s


def nth_lex_perm_rec(r, x):
    if not x:
        return []
    d, r = divmod(r, fac(len(x)-1))
    s = x.pop(d)
    return [s] + nth_lex_perm_rec(r, x)


def nth_lex_perm_iter_dm(r, x):
    s = ""
    while x:
        d, r = divmod(r, fac(len(x)-1))
        s += str(x.pop(d))  # get dth smallest
    return s


if __name__ == "__main__":
    from time import time

    start = time()
    print nth_lex_perm_iter(1000000, [0,1,2,3,4,5,6,7,8,9])
    print "Iterative time: {}".format(time() - start)

    start = time()
    print "".join(map(str, nth_lex_perm_rec(999999, [0,1,2,3,4,5,6,7,8,9])))
    print "Recursive time: {}".format(time() - start)

    start = time()
    print nth_lex_perm_iter_dm(999999, [0,1,2,3,4,5,6,7,8,9])
    print "Iterative with divmod time: {}".format(time() - start)

