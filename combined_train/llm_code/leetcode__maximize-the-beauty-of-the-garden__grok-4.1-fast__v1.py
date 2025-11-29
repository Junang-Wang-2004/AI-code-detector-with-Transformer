class C1(object):

    def maximumBeauty(self, a1):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + (a1[v3] if a1[v3] > 0 else 0)
        v4 = {}
        v5 = {}
        for v3, v6 in enumerate(a1):
            if v6 not in v4:
                v4[v6] = v3
            v5[v6] = v3
        v7 = float('-inf')
        for v6 in v4:
            if v5[v6] > v4[v6]:
                v8 = v4[v6]
                v9 = v5[v6]
                v10 = v2[v9 + 1] - v2[v8]
                v11 = 2 * v6 if v6 < 0 else 0
                v7 = max(v7, v10 + v11)
        return v7
