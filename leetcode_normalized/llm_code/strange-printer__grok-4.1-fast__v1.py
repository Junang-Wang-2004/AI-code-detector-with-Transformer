class C1:

    def strangePrinter(self, a1):
        v1 = len(a1)
        if not v1:
            return 0
        v2 = [[0] * v1 for v3 in range(v1)]
        for v4 in range(v1):
            v2[v4][v4] = 1
        for v5 in range(2, v1 + 1):
            for v6 in range(v1 - v5 + 1):
                v7 = v6 + v5 - 1
                v2[v6][v7] = v2[v6][v7 - 1] + 1
                for v8 in range(v6, v7):
                    if a1[v8] == a1[v7]:
                        v9 = v2[v8 + 1][v7 - 1] if v8 + 1 <= v7 - 1 else 0
                        v2[v6][v7] = min(v2[v6][v7], v2[v6][v8] + v9)
        return v2[0][v1 - 1]
