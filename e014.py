def collatz(n): return n/2 if n%2 == 0 else 3*n+1


def collatz_seq(n):
    s = [n]
    while n != 1:
        n = collatz(n)
        s.append(n)
    return s


def largest_collatz(n):
    s = []
    for i in xrange(1, n):
        c = collatz_seq(i)
        if len(c) > len(s):
            s = c
    return s[0]


def largest_collatz_sieve(n):
    lens = {1:1, 2:2}
    for i in xrange(3, n):
        s = []
        c = 0
        while i > 1:
            s.append(i)
            if i in lens:
                c += lens[i]
                for j in xrange(len(s)-1):
                    lens[s[j]] = c-j
                i = 0
            else:
                c += 1
                i = collatz(i)
        if s[0] not in lens:
            lens[s[0]] = c
    return max(lens.iterkeys(), key=lambda x: lens[x])


def witchcraft(n, cache={1:1}):
    if n not in cache: cache[n] = witchcraft(collatz(n)) + 1
    return cache[n]


if __name__ == "__main__":
    from time import time

    start = time()
    print max(range(1,1000000), key=witchcraft)
    print "Witchcraft time: {}".format(time() - start)

    start = time()
    print largest_collatz_sieve(1000000)
    print "Sieve time: {}".format(time() - start)

