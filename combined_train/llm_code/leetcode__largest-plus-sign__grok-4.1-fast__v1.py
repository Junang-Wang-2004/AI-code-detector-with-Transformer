class C1:

    def orderOfLargestPlusSign(self, a1, a2):
        v1 = set(map(tuple, a2))
        v2 = [[0] * a1 for v3 in range(a1)]
        for v4 in range(a1):
            v5 = 0
            for v6 in range(a1):
                v5 = 0 if (v4, v6) in v1 else v5 + 1
                v2[v4][v6] = v5
        v7 = [[0] * a1 for v3 in range(a1)]
        for v4 in range(a1):
            v5 = 0
            for v6 in range(a1 - 1, -1, -1):
                v5 = 0 if (v4, v6) in v1 else v5 + 1
                v7[v4][v6] = v5
        v8 = [[0] * a1 for v3 in range(a1)]
        for v6 in range(a1):
            v5 = 0
            for v4 in range(a1):
                v5 = 0 if (v4, v6) in v1 else v5 + 1
                v8[v4][v6] = v5
        v9 = [[0] * a1 for v3 in range(a1)]
        for v6 in range(a1):
            v5 = 0
            for v4 in range(a1 - 1, -1, -1):
                v5 = 0 if (v4, v6) in v1 else v5 + 1
                v9[v4][v6] = v5
        v10 = 0
        for v4 in range(a1):
            for v6 in range(a1):
                v11 = min(v2[v4][v6], v7[v4][v6], v8[v4][v6], v9[v4][v6])
                if v11 > v10:
                    v10 = v11
        return v10
