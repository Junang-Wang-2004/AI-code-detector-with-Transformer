class C1:

    def canDistribute(self, a1, a2):
        v1 = {}
        for v2 in a1:
            v1[v2] = v1.get(v2, 0) + 1
        v3 = sorted(v1.values(), reverse=True)
        v4 = len(a2)
        v5 = (1 << v4) - 1
        v6 = [0] * (v5 + 1)
        for v7 in range(v5 + 1):
            for v8 in range(v4):
                if v7 & 1 << v8:
                    v6[v7] += a2[v8]
        v9 = {0}
        for v10 in v3[:v4]:
            v11 = set(v9)
            for v12 in v9:
                v13 = v5 ^ v12
                v14 = v13
                while v14:
                    if v6[v14] <= v10:
                        v11.add(v12 | v14)
                    v14 = v14 - 1 & v13
            v9 = v11
        return v5 in v9
