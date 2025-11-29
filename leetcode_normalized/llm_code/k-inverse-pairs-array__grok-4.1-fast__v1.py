class C1:

    def kInversePairs(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = [0] * (a2 + 1)
        v2[0] = 1
        for v3 in range(1, a1 + 1):
            v4 = [0] * (a2 + 2)
            for v5 in range(a2 + 1):
                v4[v5 + 1] = (v4[v5] + v2[v5]) % v1
            v6 = v3 - 1
            v7 = [0] * (a2 + 1)
            for v8 in range(a2 + 1):
                v9 = max(0, v8 - v6)
                v7[v8] = (v4[v8 + 1] - v4[v9] + v1) % v1
            v2 = v7
        return v2[a2]
