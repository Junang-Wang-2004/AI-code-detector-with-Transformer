class C1:

    def checkPartitioning(self, a1):
        v1 = len(a1)
        v2 = [[False] * v1 for v3 in range(v1)]
        for v4 in range(v1):
            v2[v4][v4] = True
        for v4 in range(v1 - 1):
            if a1[v4] == a1[v4 + 1]:
                v2[v4][v4 + 1] = True
        for v5 in range(3, v1 + 1):
            for v4 in range(v1 - v5 + 1):
                v6 = v4 + v5 - 1
                if a1[v4] == a1[v6] and v2[v4 + 1][v6 - 1]:
                    v2[v4][v6] = True
        for v7 in range(1, v1 - 1):
            if not v2[0][v7 - 1]:
                continue
            for v8 in range(v7 + 1, v1):
                if v2[v7][v8 - 1] and v2[v8][v1 - 1]:
                    return True
        return False
