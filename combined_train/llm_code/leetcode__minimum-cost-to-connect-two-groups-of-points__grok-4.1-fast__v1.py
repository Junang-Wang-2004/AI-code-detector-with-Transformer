class C1:

    def connectTwoGroups(self, a1):
        v1 = len(a1)
        v2 = len(a1[0]) if v1 else 0
        v3 = 1 << v2
        v4 = float('inf')
        v5 = [v4] * v3
        v5[0] = 0
        for v6 in a1:
            v7 = [v4] * v3
            for v8 in range(v3):
                if v5[v8] == v4:
                    continue
                for v9 in range(v2):
                    v10 = v8 | 1 << v9
                    v7[v10] = min(v7[v10], v5[v8] + v6[v9])
            for v9 in range(v2):
                v11 = 1 << v9
                for v8 in range(v3):
                    if v7[v8] == v4:
                        continue
                    v10 = v8 | v11
                    v7[v10] = min(v7[v10], v7[v8] + v6[v9])
            v5 = v7
        return v5[v3 - 1]
