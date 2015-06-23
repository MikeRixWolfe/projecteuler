if __name__ == "__main__":
    from time import time

    start = time()
    print sum(map(int, list(str(2**1000))))
    print "Time: {}".format(time() - start)
