class C1:

    def minimumSum(self, a1):
        v1 = len(a1)
        v2 = 10 ** 18
        v3 = [v2] * v1
        v4 = v2
        for v5 in range(v1 - 1, -1, -1):
            v3[v5] = v4
            v4 = min(v4, a1[v5])
        v6 = v2
        v7 = v2
        for v5 in range(v1):
            if v7 < a1[v5] and a1[v5] > v3[v5]:
                v6 = min(v6, v7 + a1[v5] + v3[v5])
            v7 = min(v7, a1[v5])
        return v6 if v6 < v2 else -1
