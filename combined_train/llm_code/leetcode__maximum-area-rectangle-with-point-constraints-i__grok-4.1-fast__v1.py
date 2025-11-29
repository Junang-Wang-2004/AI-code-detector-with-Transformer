class C1:

    def maxRectangleArea(self, a1):
        a1.sort()
        v1 = sorted({p[1] for v2 in a1})
        v3 = {y: i + 1 for v4, v5 in enumerate(v1)}
        v6 = len(v1)
        v7 = [0] * (v6 + 2)

        def add(a1, a2):
            while a1 <= v6:
                v7[a1] += a2
                a1 += a1 & -a1

        def sum_upto(a1):
            v1 = 0
            while a1 > 0:
                v1 += v7[a1]
                a1 -= a1 & -a1
            return v1
        v8 = {}
        v9 = -1
        v4 = 0
        v10 = len(a1)
        while v4 < v10:
            v11 = a1[v4][0]
            v12 = v4
            while v12 < v10 and a1[v12][0] == v11:
                v12 += 1
            for v13 in range(v4, v12):
                add(v3[a1[v13][1]], 1)
            for v13 in range(v4, v12 - 1):
                v14 = a1[v13][1]
                v15 = a1[v13 + 1][1]
                v16 = v3[v14]
                v17 = v3[v15]
                v18 = sum_upto(v17) - sum_upto(v16 - 1)
                v19 = (v16, v17)
                if v19 in v8:
                    v20, v21 = v8[v19]
                    if v20 + 2 == v18:
                        v22 = (v11 - v21) * (v15 - v14)
                        v9 = max(v9, v22)
                v8[v19] = (v18, v11)
            v4 = v12
        return v9
