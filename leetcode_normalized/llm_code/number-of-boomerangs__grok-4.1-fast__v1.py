class C1:

    def numberOfBoomerangs(self, a1):
        v1 = 0
        v2 = len(a1)
        for v3 in range(v2):
            v4 = {}
            for v5 in range(v2):
                if v3 == v5:
                    continue
                v6 = a1[v3][0] - a1[v5][0]
                v7 = a1[v3][1] - a1[v5][1]
                v8 = v6 * v6 + v7 * v7
                v4[v8] = v4.get(v8, 0) + 1
            for v9 in v4.values():
                if v9 > 1:
                    v1 += v9 * (v9 - 1)
        return v1
