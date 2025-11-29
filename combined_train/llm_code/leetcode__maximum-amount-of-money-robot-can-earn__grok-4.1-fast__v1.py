class C1(object):

    def maximumAmount(self, a1):
        v1 = len(a1)
        if v1 == 0 or len(a1[0]) == 0:
            return 0
        v2 = len(a1[0])
        v3 = max(v1, v2)
        v4 = min(v1, v2)
        if v1 <= v2:
            v5 = [[a1[j][i] for v6 in range(v1)] for v7 in range(v2)]
        else:
            v5 = [row[:] for v8 in a1]
        v9 = [float('-inf')] * v4
        v9[0] = max(v5[0][0], 0)
        for v6 in range(1, v4):
            v9[v6] = v9[v6 - 1] + v5[0][v6]
        for v7 in range(1, v3):
            v10 = [float('-inf')] * v4
            v10[0] = v9[0] + v5[v7][0]
            for v6 in range(1, v4):
                v10[v6] = v5[v7][v6] + max(v9[v6], v10[v6 - 1])
            v9 = v10
        return v9[-1]
