import bisect

class C1(object):

    def closestCost(self, a1, a2, a3):
        """
        """
        v1 = 2
        v2 = set([0])
        for v3 in a2:
            v2 = set([c + i * v3 for v4 in v2 for v5 in range(v1 + 1)])
        v6, v2 = (float('inf'), sorted(v2))
        for v7 in a1:
            v8 = bisect.bisect_left(v2, a3 - v7)
            if v8 < len(v2):
                v6 = min(v6, v7 + v2[v8], key=lambda x: (abs(x - a3), x))
            if v8 > 0:
                v6 = min(v6, v7 + v2[v8 - 1], key=lambda x: (abs(x - a3), x))
        return v6
