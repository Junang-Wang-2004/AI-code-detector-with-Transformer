class C1:

    def maxValueOfCoins(self, a1, a2):
        v1 = [0] * (a2 + 1)
        for v2 in a1:
            v3 = [0] * (len(v2) + 1)
            for v4 in range(1, len(v2) + 1):
                v3[v4] = v3[v4 - 1] + v2[v4 - 1]
            for v5 in range(a2, -1, -1):
                v6 = min(a2 - v5, len(v2))
                for v7 in range(1, v6 + 1):
                    v1[v5 + v7] = max(v1[v5 + v7], v1[v5] + v3[v7])
        return v1[a2]
