import itertools

class C1(object):

    def maximumProfit(self, a1, a2, a3):
        """
        """
        v1 = [[0] * (a3 + 1) for v2 in range(2)]
        for v3, (v4, v5) in enumerate(zip(a1, a2)):
            for v6 in range(a3 + 1):
                v1[(v3 + 1) % 2][v6] = max(v1[v3 % 2][v6], v1[v3 % 2][v6 - v4] + (v5 - v4) if v6 - v4 >= 0 else 0)
        return v1[len(a1) % 2][-1]
