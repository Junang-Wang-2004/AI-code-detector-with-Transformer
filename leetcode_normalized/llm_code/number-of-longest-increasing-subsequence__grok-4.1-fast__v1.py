class C1:

    def findNumberOfLIS(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = [1] * v1
        for v3 in range(1, v1):
            for v4 in range(v3):
                if a1[v3] > a1[v4]:
                    v2[v3] = max(v2[v3], v2[v4] + 1)
        v5 = max(v2)
        v6 = [1 if v2[k] == 1 else 0 for v7 in range(v1)]
        for v3 in range(1, v1):
            for v4 in range(v3):
                if a1[v3] > a1[v4] and v2[v4] + 1 == v2[v3]:
                    v6[v3] += v6[v4]
        return sum((v6[v3] for v3 in range(v1) if v2[v3] == v5))
