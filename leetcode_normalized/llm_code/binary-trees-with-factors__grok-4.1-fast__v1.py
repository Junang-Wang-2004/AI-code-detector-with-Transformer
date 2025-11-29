class C1:

    def numFactoredBinaryTrees(self, a1):
        v1 = 10 ** 9 + 7
        v2 = sorted(a1)
        v3 = len(v2)
        if v3 == 0:
            return 0
        v4 = {v2[k]: k for v5 in range(v3)}
        v6 = [1] * v3
        v7 = 0
        for v8 in range(v3):
            for v9 in range(v8):
                if v2[v8] % v2[v9] != 0:
                    continue
                v10 = v2[v8] // v2[v9]
                if v10 in v4:
                    v6[v8] = (v6[v8] + v6[v9] * v6[v4[v10]]) % v1
            v7 = (v7 + v6[v8]) % v1
        return v7
