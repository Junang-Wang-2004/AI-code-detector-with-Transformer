class C1(object):

    def minTrioDegree(self, a1, a2):
        v1 = [[False] * (a1 + 1) for v2 in range(a1 + 1)]
        v3 = [0] * (a1 + 1)
        for v4, v5 in a2:
            v1[v4][v5] = True
            v1[v5][v4] = True
            v3[v4] += 1
            v3[v5] += 1
        v6 = float('inf')
        for v7 in range(1, a1 + 1):
            for v8 in range(v7 + 1, a1 + 1):
                if not v1[v7][v8]:
                    continue
                for v9 in range(v8 + 1, a1 + 1):
                    if v1[v7][v9] and v1[v8][v9]:
                        v6 = min(v6, v3[v7] + v3[v8] + v3[v9] - 6)
        return v6 if v6 != float('inf') else -1
