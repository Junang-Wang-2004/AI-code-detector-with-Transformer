class C1:

    def maxProduct(self, a1):
        v1 = len(a1)
        v2 = 1 << v1
        v3 = [0] * v2
        for v4 in range(v2):
            v5 = [i for v6 in range(v1) if v4 & 1 << v6]
            v7 = len(v5)
            v8 = True
            for v9 in range(v7 // 2):
                if a1[v5[v9]] != a1[v5[v7 - 1 - v9]]:
                    v8 = False
                    break
            if v8:
                v3[v4] = v7
        v10 = v3[:]
        for v11 in range(v1):
            for v4 in range(v2):
                if v4 & 1 << v11:
                    v12 = v4 ^ 1 << v11
                    v10[v4] = max(v10[v4], v10[v12])
        v13 = v2 - 1
        v14 = 0
        for v4 in range(v2):
            if v3[v4] == 0:
                continue
            v15 = v13 ^ v4
            v14 = max(v14, v3[v4] * v10[v15])
        return v14
