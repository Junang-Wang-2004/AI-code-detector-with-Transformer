class C1:

    def fullBloomFlowers(self, a1, a2):
        v1 = sorted((start for v2, v3 in a1))
        v4 = sorted((v3 + 1 for v2, v3 in a1))
        v5 = sorted(enumerate(a2), key=lambda p: p[1])
        v6 = [0] * len(a2)
        v7 = 0
        v8 = 0
        for v9, v10 in v5:
            while v7 < len(v1) and v1[v7] <= v10:
                v7 += 1
            while v8 < len(v4) and v4[v8] <= v10:
                v8 += 1
            v6[v9] = v7 - v8
        return v6
