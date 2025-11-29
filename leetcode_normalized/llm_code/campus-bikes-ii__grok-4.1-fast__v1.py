class C1:

    def assignBikes(self, a1, a2):
        v1 = len(a1)
        v2 = len(a2)
        v3 = float('inf')
        v4 = [[0] * v2 for v5 in range(v1)]
        for v6 in range(v1):
            for v7 in range(v2):
                v4[v6][v7] = abs(a1[v6][0] - a2[v7][0]) + abs(a1[v6][1] - a2[v7][1])
        v8 = [[v3] * (1 << v2) for v5 in range(v1 + 1)]
        v8[0][0] = 0
        for v6 in range(v1):
            for v9 in range(1 << v2):
                if v8[v6][v9] == v3:
                    continue
                for v7 in range(v2):
                    if v9 & 1 << v7:
                        continue
                    v10 = v9 | 1 << v7
                    v8[v6 + 1][v10] = min(v8[v6 + 1][v10], v8[v6][v9] + v4[v6][v7])
        return min(v8[v1])
