class C1(object):

    def maxProfit(self, a1, a2, a3):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v4].append(v3)
        v5 = 1 << a1
        v6 = [-1] * v5
        v6[0] = 0
        v7 = [0] * v5
        for v8 in range(v5):
            v7[v8] = v7[v8 >> 1] + (v8 & 1)
        for v9 in range(v5):
            if v6[v9] == -1:
                continue
            v10 = v7[v9] + 1
            for v11 in range(a1):
                if v9 & 1 << v11:
                    continue
                v12 = True
                for v13 in v1[v11]:
                    if not v9 & 1 << v13:
                        v12 = False
                        break
                if v12:
                    v14 = v9 | 1 << v11
                    v6[v14] = max(v6[v14], v6[v9] + v10 * a3[v11])
        return v6[v5 - 1]
