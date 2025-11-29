class C1:

    def numberWays(self, a1):
        v1 = 10 ** 9 + 7
        v2 = 40
        v3 = len(a1)
        v4 = [[] for v5 in range(v2)]
        for v6 in range(v3):
            for v7 in a1[v6]:
                v4[v7 - 1].append(v6)
        v8 = [0] * (1 << v3)
        v8[0] = 1
        for v9 in range(v2):
            v10 = v4[v9]
            if not v10:
                continue
            v11 = v8[:]
            for v12 in range(1 << v3):
                if v8[v12] == 0:
                    continue
                for v13 in v10:
                    if v12 & 1 << v13 == 0:
                        v14 = v12 | 1 << v13
                        v11[v14] = (v11[v14] + v8[v12]) % v1
            v8 = v11
        return v8[(1 << v3) - 1]
