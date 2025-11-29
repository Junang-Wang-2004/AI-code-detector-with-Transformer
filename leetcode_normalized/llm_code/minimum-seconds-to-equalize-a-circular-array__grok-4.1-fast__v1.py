class C1:

    def minimumSeconds(self, a1):
        v1 = len(a1)
        v2 = {}
        for v3, v4 in enumerate(a1):
            if v4 not in v2:
                v2[v4] = []
            v2[v4].append(v3)
        v5 = v1
        for v6 in v2.values():
            v7 = len(v6)
            if v7 == 0:
                continue
            v8 = v6[0] + v1 - v6[-1]
            for v9 in range(v7 - 1):
                v8 = max(v8, v6[v9 + 1] - v6[v9])
            v5 = min(v5, v8 // 2)
        return v5
