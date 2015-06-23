from e024 import fac

if __name__ == "__main__":
    from time import time

    start = time()
    print sum(map(int, list(str(fac(100)))))
    print "Time: {}".format(time() - start)
