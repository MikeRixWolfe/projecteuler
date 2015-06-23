triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def combine_rows(end, end_1):
    new_row = []
    for i, x in enumerate(end_1):
        new_row.append(max(end_1[i] + end[i], end_1[i] + end[i+1]))
    return new_row


def reduce_rows(tri):
    tri = [list(map(int, l.split())) for l in tri.split('\n')]
    while True:
        end = tri.pop(-1)
        end_minus_one = tri.pop(-1)
        new_end = combine_rows(end, end_minus_one)
        if len(new_end) == 1:
            return new_end[0]
        tri.append(new_end)
    return tri


def max_path_sum(tri):
    tri = [list(map(int, l.split())) for l in tri.split('\n')][::-1]
    for x in range(len(tri)):
        for y in range(len(tri[x])-1):
            tri[x+1][y] = max(tri[x][y]+tri[x+1][y], tri[x][y+1]+tri[x+1][y])
    return tri[-1][-1]


if __name__ == "__main__":
    from time import time

    start = time()
    print reduce_rows(triangle)
    print "Reducer time: {}".format(time() - start)

    start = time()
    print max_path_sum(triangle)
    print "MPS time: {}".format(time() - start)

