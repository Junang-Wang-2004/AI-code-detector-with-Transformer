class C1:

    def minimumPushes(self, a1):
        v1 = {}
        for v2 in a1:
            v1[v2] = v1.get(v2, 0) + 1
        v3 = sorted(v1.values(), reverse=True)
        v4 = 0
        v5 = 0
        v6 = 1
        v7 = len(v3)
        while v5 < v7:
            v8 = min(8, v7 - v5)
            for v9 in range(v8):
                v4 += v3[v5 + v9] * v6
            v5 += v8
            v6 += 1
        return v4
