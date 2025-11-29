class C1(object):

    def rectangleArea(self, a1):
        v1 = 10 ** 9 + 7
        v2 = []
        v3 = set()
        for v4, v5, v6, v7 in a1:
            v2.append((v5, 1, v4, v6))
            v2.append((v7, -1, v4, v6))
            v3.add(v4)
            v3.add(v6)
        v8 = sorted(v3)
        v9 = len(v8)
        if v9 < 2:
            return 0
        v10 = {v8[i]: i for v11 in range(v9)}
        v12 = v9 - 1
        v13 = 4 * v9
        v14 = [0] * v13
        v15 = [0] * v13
        v16 = [0] * v13
        v17 = [v8[v11 + 1] - v8[v11] for v11 in range(v12)]

        def construct(a1, a2, a3):
            if a2 == a3:
                v16[a1] = v17[a2]
                return
            v1 = (a2 + a3) // 2
            construct(2 * a1, a2, v1)
            construct(2 * a1 + 1, v1 + 1, a3)
            v16[a1] = v16[2 * a1] + v16[2 * a1 + 1]
        construct(1, 0, v12 - 1)

        def modify(a1, a2, a3, a4, a5, a6):
            if a4 > a3 or a5 < a2:
                return
            if a4 <= a2 and a3 <= a5:
                v14[a1] += a6
            else:
                v1 = (a2 + a3) // 2
                modify(2 * a1, a2, v1, a4, a5, a6)
                modify(2 * a1 + 1, v1 + 1, a3, a4, a5, a6)
            if v14[a1] > 0:
                v15[a1] = v16[a1]
            elif a2 == a3:
                v15[a1] = 0
            else:
                v15[a1] = v15[2 * a1] + v15[2 * a1 + 1]
        v2.sort()
        v18 = 0
        v19 = v2[0][0]
        v20 = 0
        for v21, v22, v23, v24 in v2:
            v18 = (v18 + v20 * (v21 - v19)) % v1
            v25 = v10[v23]
            v26 = v10[v24] - 1
            if v25 <= v26:
                modify(1, 0, v12 - 1, v25, v26, v22)
            v20 = v15[1]
            v19 = v21
        return v18
