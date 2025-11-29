import itertools

class C1(object):

    def maximumProfit(self, a1, a2, a3):
        """
        """
        v1 = [0] * (a3 + 1)
        for v2, (v3, v4) in enumerate(zip(a1, a2)):
            if v4 - v3 < 0:
                continue
            for v5 in reversed(range(v3, a3 + 1)):
                v1[v5] = max(v1[v5], v1[v5 - v3] + (v4 - v3))
        return v1[-1]
