class C1(object):

    def minCost(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = [[[float('inf') for v2 in range(a4)] for v2 in range(a5)] for v2 in range(2)]
        for v3 in range(a3):
            v1[v3 % 2] = [[float('inf') for v2 in range(a4)] for v2 in range(a5)]
            for v4 in range(min(a5, v3 + 1)):
                for v5 in range(a4):
                    if a1[v3] and a1[v3] - 1 != v5:
                        continue
                    v6 = v1[(v3 - 1) % 2][v4][v5] if v3 - 1 >= 0 else 0
                    v7 = (min([v1[(v3 - 1) % 2][v4 - 1][nk] for v8 in range(a4) if v8 != v5] or [float('inf')]) if v4 - 1 >= 0 else float('inf')) if v3 - 1 >= 0 else 0
                    v9 = a2[v3][v5] if not a1[v3] else 0
                    v1[v3 % 2][v4][v5] = min(v6, v7) + v9
        v10 = min(v1[(a3 - 1) % 2][-1])
        return v10 if v10 != float('inf') else -1
