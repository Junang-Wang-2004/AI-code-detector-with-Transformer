class C1(object):

    def minChanges(self, a1, a2):
        v1 = len(a1)
        v2 = v1 // 2
        v3 = [0] * (a2 + 1)
        v4 = [0] * (a2 + 1)
        for v5 in range(v2):
            v6 = a1[v5]
            v7 = a1[v1 - 1 - v5]
            v8 = abs(v6 - v7)
            v9 = max(v6, a2 - v6, v7, a2 - v7)
            v3[v8] += 1
            v4[v9] += 1
        v10 = [0] * (a2 + 2)
        v11 = 0
        for v12 in range(a2 + 1):
            v10[v12] = v11
            v11 += v4[v12]
        v13 = v2
        for v12 in range(a2 + 1):
            v14 = v2 - v3[v12] + v10[v12]
            if v14 < v13:
                v13 = v14
        return v13
