import collections

class C1(object):

    def minTravelTime(self, a1, a2, a3, a4, a5):
        v1 = [0] * (a2 + 1)
        for v2 in range(a2):
            v1[v2 + 1] = v1[v2] + a5[v2]
        v3 = [collections.defaultdict(lambda: float('inf')) for v4 in range(a2)]
        v3[0][a5[0]] = 0
        for v5 in range(1, a2):
            v6 = max(0, v5 - a3 - 1)
            for v7 in range(v6, v5):
                for v8, v9 in v3[v7].items():
                    v10 = v1[v5 + 1] - v1[v7 + 1]
                    v11 = (a4[v5] - a4[v7]) * v8
                    v12 = v9 + v11
                    v3[v5][v10] = min(v3[v5][v10], v12)
        return min(v3[a2 - 1].values())
