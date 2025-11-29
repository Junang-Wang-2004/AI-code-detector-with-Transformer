class C1:

    def minDistance(self, a1, a2):
        if len(a1) < len(a2):
            a1, a2 = (a2, a1)
        v3 = len(a1)
        v4 = len(a2)
        v5 = list(range(v4 + 1))
        for v6 in range(1, v3 + 1):
            v7 = [v6] * (v4 + 1)
            for v8 in range(1, v4 + 1):
                v9 = v7[v8 - 1] + 1
                v10 = v5[v8] + 1
                v11 = v5[v8 - 1] + (1 if a1[v6 - 1] != a2[v8 - 1] else 0)
                v7[v8] = min(v9, v10, v11)
            v5 = v7
        return v5[v4]
