class C1:

    def maxScore(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * (a2 + 1)
        for v3 in range(1, a2 + 1):
            v2[v3] = v2[v3 - 1] + a1[v3 - 1]
        v4 = [0] * (a2 + 1)
        for v3 in range(1, a2 + 1):
            v4[v3] = v4[v3 - 1] + a1[v1 - v3]
        v5 = 0
        for v3 in range(a2 + 1):
            v5 = max(v5, v2[v3] + v4[a2 - v3])
        return v5
