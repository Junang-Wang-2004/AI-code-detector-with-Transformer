import collections

class C1(object):

    def minTravelTime(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = [0] * (a2 + 1)
        for v2 in range(a2):
            v1[v2 + 1] = v1[v2] + a5[v2]
        v3 = collections.defaultdict(lambda: collections.defaultdict(lambda: float('inf')))
        v3[0][a5[0]] = 0
        for v4 in range(2, a2 - a3 + 1):
            v5 = collections.defaultdict(lambda: collections.defaultdict(lambda: float('inf')))
            for v2 in range(v4 - 1, v4 - 1 + (a3 + 1)):
                for v6 in range(v4 - 2, v2):
                    for v7, v8 in v3[v6].items():
                        v5[v2][v1[v2 + 1] - v1[v6 + 1]] = min(v5[v2][v1[v2 + 1] - v1[v6 + 1]], (a4[v2] - a4[v6]) * v7 + v8)
            v3 = v5
        return min(v3[a2 - 1].values())
