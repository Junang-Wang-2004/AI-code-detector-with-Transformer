class C1:

    def getMaximumGold(self, a1):
        if not a1:
            return 0
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = [[False] * v2 for v4 in range(v1)]
        v5 = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def explore(a1, a2):
            v3[a1][a2] = True
            v1 = 0
            for v2, v3 in v5:
                v4 = a1 + v2
                v5 = a2 + v3
                if 0 <= v4 < v1 and 0 <= v5 < v2 and (a1[v4][v5] > 0) and (not v3[v4][v5]):
                    v1 = max(v1, explore(v4, v5))
            v3[a1][a2] = False
            return a1[a1][a2] + v1
        v6 = 0
        for v7 in range(v1):
            for v8 in range(v2):
                if a1[v7][v8] > 0:
                    v6 = max(v6, explore(v7, v8))
        return v6
