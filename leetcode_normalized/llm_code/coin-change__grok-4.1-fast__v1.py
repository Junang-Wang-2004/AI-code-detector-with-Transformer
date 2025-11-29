class C1:

    def coinChange(self, a1, a2):
        v1 = a2
        v2 = 10 ** 9
        v3 = [v2] * (v1 + 1)
        v3[0] = 0
        for v4 in a1:
            for v5 in range(v4, v1 + 1):
                v3[v5] = min(v3[v5], v3[v5 - v4] + 1)
        v6 = v3[v1]
        return v6 if v6 < v2 else -1
