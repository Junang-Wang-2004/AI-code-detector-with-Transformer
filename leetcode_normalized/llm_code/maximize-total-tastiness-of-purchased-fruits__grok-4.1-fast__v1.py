class C1:

    def maxTastiness(self, a1, a2, a3, a4):
        v1 = [[0] * (a4 + 1) for v2 in range(a3 + 1)]
        v3 = len(a1)
        for v4 in range(v3):
            v5 = a1[v4]
            v6 = a2[v4]
            v7 = v5 // 2
            for v8 in range(a3, -1, -1):
                for v9 in range(a4, -1, -1):
                    if v8 >= v5:
                        v1[v8][v9] = max(v1[v8][v9], v6 + v1[v8 - v5][v9])
                    if v9 > 0 and v8 >= v7:
                        v1[v8][v9] = max(v1[v8][v9], v6 + v1[v8 - v7][v9 - 1])
        return v1[a3][a4]
