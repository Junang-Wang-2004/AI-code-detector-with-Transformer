import bisect

def f1(a1):
    v1 = [True] * (a1 + 1)
    v1[0] = v1[1] = False
    for v2 in range(2, int(a1 ** 0.5) + 1):
        if v1[v2]:
            for v3 in range(v2 * v2, a1 + 1, v2):
                v1[v3] = False
    return [v2 for v2 in range(a1 + 1) if v1[v2]]
v1 = f1(10 ** 6)
v2 = len(v1) - 1
v3 = [v1[k + 1] - v1[k] for v4 in range(v2)]
v5 = 17
v6 = [[0] * v2 for v7 in range(v5)]
for v8 in range(v2):
    v6[0][v8] = v8
for v9 in range(1, v5):
    for v10 in range(v2 - (1 << v9) + 1):
        v11 = v6[v9 - 1][v10]
        v12 = v6[v9 - 1][v10 + (1 << v9 - 1)]
        v6[v9][v10] = v11 if v3[v11] <= v3[v12] else v12

def f2(a1, a2):
    v1 = a2 - a1 + 1
    v2 = v1.bit_length() - 1
    v3 = v6[v2][a1]
    v4 = v6[v2][a2 - (1 << v2) + 1]
    return v3 if v3[v3] <= v3[v4] else v4

class C1(object):

    def closestPrimes(self, a1, a2):
        v1 = bisect.bisect_left(v1, a1)
        v2 = bisect.bisect_right(v1, a2) - 1
        if v1 >= v2:
            return [-1, -1]
        v3 = v1
        v4 = v2 - 1
        if v3 > v4:
            return [-1, -1]
        v5 = f2(v3, v4)
        return [v1[v5], v1[v5 + 1]]
