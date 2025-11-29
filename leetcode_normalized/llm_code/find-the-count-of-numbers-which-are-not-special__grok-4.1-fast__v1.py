import bisect

def f1(a1):
    v1 = [True] * (a1 + 1)
    v1[0] = v1[1] = False
    for v2 in range(2, int(a1 ** 0.5) + 1):
        if v1[v2]:
            for v3 in range(v2 * v2, a1 + 1, v2):
                v1[v3] = False
    return [v2 for v2 in range(2, a1 + 1) if v1[v2]]
v1 = 10 ** 9
v2 = int(v1 ** 0.5)
v3 = f1(v2)
v4 = [p * p for v5 in v3]

class C1(object):

    def nonSpecialCount(self, a1, a2):
        v1 = bisect.bisect_right(v4, a2) - bisect.bisect_left(v4, a1)
        return a2 - a1 + 1 - v1
