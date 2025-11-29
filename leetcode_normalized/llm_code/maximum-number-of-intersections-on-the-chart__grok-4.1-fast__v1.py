class C1(object):

    def maxIntersectionCount(self, a1):
        v1 = {}
        v2 = len(a1)
        for v3 in range(v2 - 1):
            v4 = a1[v3]
            v5 = a1[v3 + 1]
            v6 = 2 * v4
            v7 = 2 * v5 + (-1 if v4 < v5 else 1)
            v8 = min(v6, v7)
            v9 = max(v6, v7) + 1
            v1[v8] = v1.get(v8, 0) + 1
            v1[v9] = v1.get(v9, 0) - 1
        v10 = a1[v2 - 1]
        v8 = 2 * v10
        v9 = v8 + 1
        v1[v8] = v1.get(v8, 0) + 1
        v1[v9] = v1.get(v9, 0) - 1
        v11 = sorted(v1)
        v12 = 0
        v13 = 0
        for v14 in v11:
            v12 += v1[v14]
            if v12 > v13:
                v13 = v12
        return v13
