import bisect

class C1(object):

    def maxValue(self, a1, a2):
        """
        """
        a1.sort()
        v1 = [x[0] for v2 in a1]
        v3 = [[0] * (a2 + 1) for v4 in range(len(a1) + 1)]
        for v5 in reversed(range(len(a1))):
            v6 = bisect.bisect_right(v1, a1[v5][1]) - 1
            for v7 in range(1, a2 + 1):
                v3[v5][v7] = max(v3[v5 + 1][v7], v3[v6 + 1][v7 - 1] + a1[v5][2])
        return v3[0][-1]
