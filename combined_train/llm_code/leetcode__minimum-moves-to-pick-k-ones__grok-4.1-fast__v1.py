class C1(object):

    def minimumMoves(self, a1, a2, a3):
        v1 = []
        for v2 in range(len(a1)):
            if a1[v2]:
                v1.append(v2)
        v3 = len(v1)
        v4 = [0] * (v3 + 1)
        for v5 in range(v3):
            v4[v5 + 1] = v4[v5] + v1[v5]
        v6 = float('inf')
        for v7 in range(min(a2, a3) + 1):
            v8 = a2 - v7
            if v8 > v3 or v8 <= 0:
                continue
            v9 = v7 * 2
            v10 = v8
            v11 = v10 // 2
            for v12 in range(v3 - v10 + 1):
                v13 = v4[v12 + v11] - v4[v12]
                v14 = v4[v12 + v10] - v4[v12 + v10 - v11]
                v15 = v14 - v13
                v6 = min(v6, v9 + v15)
        return v6
