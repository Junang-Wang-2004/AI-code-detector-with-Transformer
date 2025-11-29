class C1:

    def maxScore(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = [num for v3 in a1 for v4 in v3]
        if not v2:
            return 0
        v5 = max(v2)
        v6 = [[] for v7 in range(v5)]
        for v8 in range(v1):
            for v9 in set(a1[v8]):
                v10 = v9 - 1
                if 0 <= v10 < v5:
                    v6[v10].append(v8)
        v11 = 1 << v1
        v12 = [-float('inf')] * v11
        v12[0] = 0
        for v13 in range(v5):
            v14 = v6[v13]
            if not v14:
                continue
            for v15 in range(v11 - 1, -1, -1):
                v16 = v12[v15]
                if v16 == -float('inf'):
                    continue
                for v17 in v14:
                    if v15 & 1 << v17 == 0:
                        v18 = v15 | 1 << v17
                        v12[v18] = max(v12[v18], v16 + v13 + 1)
        return max(v12)
