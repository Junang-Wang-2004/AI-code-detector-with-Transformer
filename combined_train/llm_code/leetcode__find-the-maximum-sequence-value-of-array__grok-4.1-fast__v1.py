class C1(object):

    def maxValue(self, a1, a2):
        v1 = len(a1)
        v2 = 128
        v3 = 10 ** 9
        v4 = [v3] * v2
        v5 = [0] * v2
        v6 = [v1] * v2
        for v7 in range(v1):
            v8 = a1[v7]
            v4[v8] = 1
            for v9 in range(v2):
                if v8 & v9 == v8:
                    v5[v9] += 1
                v4[v9 | v8] = min(v4[v9 | v8], v4[v9] + 1)
            for v9 in range(v2):
                if v5[v9] >= a2 and v4[v9] <= a2 and (v6[v9] == v1):
                    v6[v9] = v7
        v10 = [v3] * v2
        v11 = [0] * v2
        v12 = [-1] * v2
        for v7 in range(v1 - 1, -1, -1):
            v8 = a1[v7]
            v10[v8] = 1
            for v9 in range(v2):
                if v8 & v9 == v8:
                    v11[v9] += 1
                v10[v9 | v8] = min(v10[v9 | v8], v10[v9] + 1)
            for v9 in range(v2):
                if v11[v9] >= a2 and v10[v9] <= a2 and (v12[v9] == -1):
                    v12[v9] = v7
        for v13 in range(v2 - 1, -1, -1):
            for v14 in range(1, v2):
                v15 = v13 ^ v14
                if v6[v14] < v12[v15]:
                    return v13
        return 0
