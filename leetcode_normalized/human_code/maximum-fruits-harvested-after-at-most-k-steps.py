class C1(object):

    def maxTotalFruits(self, a1, a2, a3):
        """
        """
        v1 = max(a2, a1[-1][0])
        v2 = [0] * (1 + v1)
        for v3, v4 in a1:
            v2[v3] = v4
        v5 = [0]
        for v6 in v2:
            v5.append(v5[-1] + v6)
        v7 = 0
        for v8 in range(min(a2, a3) + 1):
            v9 = max(a3 - 2 * v8, 0)
            v10, v11 = (a2 - v8, min(a2 + v9, v1))
            v7 = max(v7, v5[v11 + 1] - v5[v10])
        for v9 in range(min(v1 - a2, a3) + 1):
            v8 = max(a3 - 2 * v9, 0)
            v10, v11 = (max(a2 - v8, 0), a2 + v9)
            v7 = max(v7, v5[v11 + 1] - v5[v10])
        return v7
