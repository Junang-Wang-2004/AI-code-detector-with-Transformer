class C1(object):

    def minCostConnectPoints(self, a1):
        """
        """
        v1, v2 = (0, 0)
        v3 = [float('inf')] * len(a1)
        v4 = set()
        for v5 in range(len(a1) - 1):
            v6, v7 = a1[v2]
            v4.add(v2)
            for v8, (v9, v10) in enumerate(a1):
                if v8 in v4:
                    continue
                v3[v8] = min(v3[v8], abs(v9 - v6) + abs(v10 - v7))
            v11, v2 = min(((v11, v8) for v8, v11 in enumerate(v3)))
            v3[v2] = float('inf')
            v1 += v11
        return v1
