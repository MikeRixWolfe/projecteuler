from e018 import max_path_sum

if __name__ == "__main__":
    from time import time

    with open('p067_triangle.txt', 'rw') as f:
        triangle = f.read()

    start = time()
    print max_path_sum(triangle)
    print "Time: {}".format(time() - start)
