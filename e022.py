with open('p022_names.txt', 'r') as f:
    names_txt = f.read().strip('"').split('","')


def score_names(names):
    names.sort()
    s = 0
    for i, name in enumerate(names):
        s += (i+1) * sum([ord(letter)-64 for letter in name])
    return s


if __name__ == "__main__":
    from time import time

    start = time()
    print score_names(names_txt)
    print "Time: {}".format(time() - start)
