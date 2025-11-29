class C1(object):

    def maxSumOfThreeSubarrays(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = v1 - a2 + 1
        if v4 < 3:
            return []
        v5 = [v2[j + a2] - v2[j] for v6 in range(v4)]
        v7 = [0.0] * v4
        v8 = [0] * v4
        v7[0] = v5[0]
        v8[0] = 0
        for v6 in range(1, v4):
            if v5[v6] > v7[v6 - 1]:
                v7[v6] = v5[v6]
                v8[v6] = v6
            else:
                v7[v6] = v7[v6 - 1]
                v8[v6] = v8[v6 - 1]
        v9 = [0.0] * v4
        v10 = [0] * v4
        v9[v4 - 1] = v5[v4 - 1]
        v10[v4 - 1] = v4 - 1
        for v6 in range(v4 - 2, -1, -1):
            if v5[v6] > v9[v6 + 1]:
                v9[v6] = v5[v6]
                v10[v6] = v6
            else:
                v9[v6] = v9[v6 + 1]
                v10[v6] = v10[v6 + 1]
        v11 = 0
        v12 = []
        for v13 in range(a2, v1 - 2 * a2 + 1):
            v14 = v13 - a2
            v15 = v13 + a2
            v16 = v7[v14] + v5[v13] + v9[v15]
            if v16 > v11:
                v11 = v16
                v12 = [v8[v14], v13, v10[v15]]
        return v12
