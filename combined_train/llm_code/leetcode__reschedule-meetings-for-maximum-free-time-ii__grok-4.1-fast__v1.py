class C1(object):

    def maxFreeTime(self, a1, a2, a3):
        v1 = a2 + [a1]
        v2 = [0] + a3
        v3 = len(v1)
        v4 = [v1[j] - v2[j] for v5 in range(v3)]
        v6 = v7 = v8 = float('-inf')
        v9 = v10 = v11 = -1
        for v5 in range(v3):
            v12 = v4[v5]
            if v12 > v6:
                v8, v11 = (v7, v10)
                v7, v10 = (v6, v9)
                v6, v9 = (v12, v5)
            elif v12 > v7:
                v8, v11 = (v7, v10)
                v7, v10 = (v12, v5)
            elif v12 > v8:
                v8, v11 = (v12, v5)
        v13 = [(v6, v9), (v7, v10), (v8, v11)]
        v14 = 0
        for v15 in range(v3 - 1):
            v16 = v4[v15]
            v17 = v4[v15 + 1]
            v18 = v16 + v17
            v19 = v2[v15 + 1] - v1[v15]
            v20 = any((idx != v15 and idx != v15 + 1 and (v19 <= tg) for v21, v22 in v13))
            v23 = v18 + v19 if v20 else v18
            if v23 > v14:
                v14 = v23
        return v14
