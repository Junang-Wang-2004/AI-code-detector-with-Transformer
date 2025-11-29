class C1:

    def minAbsDiff(self, a1, a2):
        if not a1 or a2 == 0:
            return []
        v1, v2 = (len(a1), len(a1[0]))
        v3 = []
        for v4 in range(v1 - a2 + 1):
            v5 = []
            for v6 in range(v2 - a2 + 1):
                v7 = []
                for v8 in range(v4, v4 + a2):
                    for v9 in range(v6, v6 + a2):
                        v7.append(a1[v8][v9])
                v7.sort()
                v10 = float('inf')
                for v11 in range(1, len(v7)):
                    if v7[v11] != v7[v11 - 1]:
                        v10 = min(v10, v7[v11] - v7[v11 - 1])
                v5.append(0 if v10 == float('inf') else v10)
            v3.append(v5)
        return v3
