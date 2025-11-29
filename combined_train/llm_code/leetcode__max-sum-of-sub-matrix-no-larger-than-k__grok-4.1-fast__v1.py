from bisect import bisect_left, insort

class C1:

    def maxSumSubmatrix(self, a1, a2):
        if not a1 or not a1[0]:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = float('-inf')
        if v1 > v2:
            a1 = [list(t) for v5 in zip(*a1)]
            v1, v2 = (v2, v1)
        for v6 in range(v1):
            v7 = [0] * v2
            for v8 in range(v6, v1):
                for v9 in range(v2):
                    v7[v9] += a1[v8][v9]
                v10 = [0]
                v11 = 0
                for v12 in v7:
                    v11 += v12
                    v13 = bisect_left(v10, v11 - a2)
                    if v13 < len(v10):
                        v3 = max(v3, v11 - v10[v13])
                    insort(v10, v11)
        return v3
