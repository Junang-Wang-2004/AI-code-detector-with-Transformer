import itertools

class C1:

    def maxSumRangeQuery(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = [0] * v2
        for v4, v5 in a2:
            v3[v4] += 1
            if v5 + 1 < v2:
                v3[v5 + 1] -= 1
        v6 = list(itertools.accumulate(v3))
        v7 = sorted(a1)
        v8 = sorted(v6)
        v9 = 0
        for v10, v11 in zip(v7, v8):
            v9 = (v9 + v10 * v11) % v1
        return v9
