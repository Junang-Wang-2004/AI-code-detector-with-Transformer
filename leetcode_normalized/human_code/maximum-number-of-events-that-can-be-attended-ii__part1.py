import bisect

class C1(object):

    def maxValue(self, a1, a2):
        """
        """
        a1.sort(key=lambda x: x[1])
        v1 = [x[1] for v2 in a1]
        v3 = [[0] * (a2 + 1) for v4 in range(len(a1) + 1)]
        for v5 in range(1, len(a1) + 1):
            v6 = bisect.bisect_left(v1, a1[v5 - 1][0]) - 1
            for v7 in range(1, a2 + 1):
                v3[v5][v7] = max(v3[v5 - 1][v7], v3[v6 + 1][v7 - 1] + a1[v5 - 1][2])
        return v3[-1][-1]
