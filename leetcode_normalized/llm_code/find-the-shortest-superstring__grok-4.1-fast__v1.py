class C1:

    def shortestSuperstring(self, a1):
        v1 = len(a1)
        v2 = [[0] * v1 for v3 in range(v1)]
        for v4 in range(v1):
            for v5 in range(v1):
                v6, v7 = (len(a1[v4]), len(a1[v5]))
                for v8 in range(min(v6, v7), -1, -1):
                    if a1[v4][-v8:] == a1[v5][:v8]:
                        v2[v4][v5] = v8
                        break
        v9 = 10 ** 9
        v10 = [[v9] * v1 for v3 in range(1 << v1)]
        v11 = [[-1] * v1 for v3 in range(1 << v1)]
        for v4 in range(v1):
            v12 = 1 << v4
            v10[v12][v4] = len(a1[v4])
        for v12 in range(1 << v1):
            for v13 in range(v1):
                if v12 & 1 << v13 == 0 or v10[v12][v13] == v9:
                    continue
                for v14 in range(v1):
                    if v12 & 1 << v14:
                        continue
                    v15 = v12 | 1 << v14
                    v16 = len(a1[v14]) - v2[v13][v14]
                    v17 = v10[v12][v13] + v16
                    if v17 < v10[v15][v14]:
                        v10[v15][v14] = v17
                        v11[v15][v14] = v13
        v18 = (1 << v1) - 1
        v19 = v9
        v20 = -1
        for v5 in range(v1):
            if v10[v18][v5] < v19:
                v19 = v10[v18][v5]
                v20 = v5
        v21 = []
        v22 = v18
        v23 = v20
        while v23 != -1:
            v21.append(v23)
            v24 = v11[v22][v23]
            v22 ^= 1 << v23
            v23 = v24
        v21.reverse()
        if not v21:
            return ''
        v25 = a1[v21[0]]
        for v26 in range(1, len(v21)):
            v27 = v21[v26 - 1]
            v28 = v2[v27][v21[v26]]
            v25 += a1[v21[v26]][v28:]
        return v25
