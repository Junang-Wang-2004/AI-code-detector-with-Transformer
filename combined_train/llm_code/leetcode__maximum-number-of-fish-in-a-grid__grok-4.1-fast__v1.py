class C1:

    def findMaxFish(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = len(a1[0])
        v3 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def explore(a1, a2):
            v1 = a1[a1][a2]
            a1[a1][a2] = 0
            for v2, v3 in v3:
                v4 = a1 + v2
                v5 = a2 + v3
                if 0 <= v4 < v1 and 0 <= v5 < v2 and (a1[v4][v5] > 0):
                    v1 += explore(v4, v5)
            return v1
        v4 = 0
        for v5 in range(v1):
            for v6 in range(v2):
                if a1[v5][v6] > 0:
                    v4 = max(v4, explore(v5, v6))
        return v4
