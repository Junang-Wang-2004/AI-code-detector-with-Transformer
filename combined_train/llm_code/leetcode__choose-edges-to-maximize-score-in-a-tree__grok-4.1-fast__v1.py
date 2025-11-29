class C1:

    def maxScore(self, a1):
        v1 = len(a1)
        v2 = [[] for v3 in range(v1)]
        for v4 in range(1, v1):
            v5, v6 = a1[v4]
            v2[v5].append((v4, v6))

        def compute(a1):
            v1 = [compute(child) for v2, v3 in v2[a1]]
            if not v1:
                return (0, 0)
            v3 = [max(covered, uncovered) for v4, v5 in v1]
            v6 = sum(v3)
            v7 = float('-inf')
            for v8, (v2, v9) in enumerate(v2[a1]):
                v10, v11 = v1[v8]
                v12 = v3[v8]
                v13 = v6 - v12 + v11 + v9
                if v13 > v7:
                    v7 = v13
            return (v7, v6)
        v7, v8 = compute(0)
        return max(v7, v8)
