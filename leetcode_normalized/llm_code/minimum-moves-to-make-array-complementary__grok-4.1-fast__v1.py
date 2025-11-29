class C1(object):

    def minMoves(self, a1, a2):
        v1 = len(a1) // 2
        v2 = 2 * a2 + 2
        v3 = [0] * (v2 + 1)
        v4 = [0] * (v2 + 1)
        v5 = len(a1)
        for v6 in range(v1):
            v7 = a1[v6]
            v8 = a1[v5 - 1 - v6]
            v9 = min(v7, v8)
            v10 = max(v7, v8)
            v11 = v9 + 1
            v12 = v10 + a2
            v3[v11] += 1
            if v12 + 1 <= v2:
                v3[v12 + 1] -= 1
            v13 = v7 + v8
            if v13 <= v2:
                v4[v13] += 1
        v14 = 0
        v15 = 0
        for v16 in range(2, 2 * a2 + 1):
            v14 += v3[v16]
            v17 = v14 + v4[v16]
            if v17 > v15:
                v15 = v17
        return 2 * v1 - v15
