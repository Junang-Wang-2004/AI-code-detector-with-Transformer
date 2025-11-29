class C1(object):

    def maxTotalFruits(self, a1, a2, a3):
        v1 = max(a2, max((p for v2, v3 in a1), default=a2))
        v4 = [0] * (v1 + 1)
        for v5, v6 in a1:
            v4[v5] = v6
        v7 = [0] * (v1 + 2)
        for v8 in range(1, v1 + 2):
            v7[v8] = v7[v8 - 1] + v4[v8 - 1]
        v9 = 0
        for v10 in range(a2 + 1):
            v11 = a2 - v10
            if v11 < 0:
                break
            v12 = a3 - 2 * v10
            v13 = (a3 - v10) // 2
            v14 = max(0, v12, v13)
            v15 = min(v1, a2 + v14)
            v16 = v7[v15 + 1] - v7[v11]
            if v16 > v9:
                v9 = v16
        return v9
