class C1(object):

    def maxBuilding(self, a1, a2):
        v1 = a2 + [[1, 0], [a1, a1 - 1]]
        v1.sort(key=lambda x: x[0])
        v2 = len(v1)
        v3 = [b[0] for v4 in v1]
        v5 = [v4[1] for v4 in v1]
        v6 = v5[:]
        for v7 in range(1, v2):
            v6[v7] = min(v6[v7], v6[v7 - 1] + v3[v7] - v3[v7 - 1])
        v8 = v5[:]
        for v7 in range(v2 - 2, -1, -1):
            v8[v7] = min(v8[v7], v8[v7 + 1] + v3[v7 + 1] - v3[v7])
        v9 = 0
        for v7 in range(1, v2):
            v10 = v3[v7] - v3[v7 - 1]
            v11 = min(v6[v7 - 1], v8[v7 - 1])
            v12 = min(v6[v7], v8[v7])
            v13 = max(v11, v12) + (v10 - abs(v11 - v12)) // 2
            v9 = max(v9, v13)
        return v9
