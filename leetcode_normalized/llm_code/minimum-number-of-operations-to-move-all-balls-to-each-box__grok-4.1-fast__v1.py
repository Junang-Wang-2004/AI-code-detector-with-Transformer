class C1:

    def minOperations(self, a1):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        v3 = [0] * (v1 + 1)
        for v4 in range(v1):
            v5 = 1 if a1[v4] == '1' else 0
            v2[v4 + 1] = v2[v4] + v5
            v3[v4 + 1] = v3[v4] + v4 * v5
        v6 = v2[v1]
        v7 = v3[v1]
        v8 = [0] * v1
        for v9 in range(v1):
            v10 = v2[v9]
            v11 = v3[v9]
            v12 = v6 - v10
            v13 = v7 - v11
            v8[v9] = v9 * v10 - v11 + v13 - v9 * v12
        return v8
