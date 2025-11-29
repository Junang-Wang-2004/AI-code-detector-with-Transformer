class C1:

    def minOperations(self, a1, a2):
        v1, v2 = (len(a1), len(a2))
        if v1 < v2:
            a1, a2 = (a2, a1)
            v1, v2 = (v2, v1)
        v5 = 0
        v6 = [0] * (v2 + 1)
        for v7 in range(1, v1 + 1):
            v8 = [0] * (v2 + 1)
            for v9 in range(1, v2 + 1):
                if a1[v7 - 1] == a2[v9 - 1]:
                    v8[v9] = v6[v9 - 1] + 1
                    v5 = max(v5, v8[v9])
            v6 = v8
        return v1 + v2 - 2 * v5
