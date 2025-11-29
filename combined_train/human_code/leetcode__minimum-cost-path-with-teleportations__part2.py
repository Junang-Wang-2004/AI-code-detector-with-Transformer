class C1(object):

    def minCost(self, a1, a2):
        """
        """
        v1 = [[float('inf')] * len(a1[0]) for v2 in range(len(a1))]
        v1[-1][-1] = 0
        v3 = max((max(row) for v4 in a1))
        v5 = [float('inf')] * (v3 + 1)
        for v6 in range(a2 + 1):
            for v7 in reversed(range(len(a1))):
                for v8 in reversed(range(len(a1[0]))):
                    if v7 + 1 < len(a1):
                        v1[v7][v8] = min(v1[v7][v8], v1[v7 + 1][v8] + a1[v7 + 1][v8])
                    if v8 + 1 < len(a1[0]):
                        v1[v7][v8] = min(v1[v7][v8], v1[v7][v8 + 1] + a1[v7][v8 + 1])
                    v1[v7][v8] = min(v1[v7][v8], v5[a1[v7][v8]])
            for v7 in range(len(a1)):
                for v8 in range(len(a1[0])):
                    v5[a1[v7][v8]] = min(v5[a1[v7][v8]], v1[v7][v8])
            for v6 in range(len(v5) - 1):
                v5[v6 + 1] = min(v5[v6 + 1], v5[v6])
        return v1[0][0]
