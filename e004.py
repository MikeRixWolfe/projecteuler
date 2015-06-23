def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


def largest_pal_n_digits(n):
    s = 0
    for i in xrange(10**(n-1), 10**n):
        for j in xrange(10**(n-1), 10**n):
            if is_palindrome(i*j) and i*j > s:
                s = i*j
    return s

if __name__ == "__main__":
    from time import time

    start = time()
    print largest_pal_n_digits(3)
    print "Time: {}".format(time() - start)
