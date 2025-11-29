from bisect import bisect_left, insort

class C1(object):

    def maxSumSubmatrix(self, a1, a2):
        """
        """
        if not a1:
            return 0
        v1 = min(len(a1), len(a1[0]))
        v2 = max(len(a1), len(a1[0]))
        v3 = float('-inf')
        for v4 in range(v1):
            v5 = [0] * v2
            for v6 in range(v4, v1):
                for v7 in range(v2):
                    v5[v7] += a1[v6][v7] if v1 == len(a1) else a1[v7][v6]
                v8, v9 = ([0], 0)
                for sum in v5:
                    v9 += sum
                    v10 = bisect_left(v8, v9 - a2)
                    if v10 != len(v8):
                        v3 = max(v3, v9 - v8[v10])
                    insort(v8, v9)
        return v3
