from e003 import is_prime


def nth_prime(n):
    i, j = 1, 0
    while j < n:
        i += 1
        if is_prime(i):
            j += 1
    return i


if __name__ == "__main__":
    from time import time

    start = time()
    print nth_prime(10001)
    print "Time: {}".format(time() - start)

