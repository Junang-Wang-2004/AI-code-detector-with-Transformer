class C1:

    def getMinDistSum(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0.0
        v2 = sum((x for v3, v4 in a1)) / v1
        v5 = sum((y for v4, v6 in a1)) / v1
        v7 = [v2, v5]
        v8 = 1e-06
        while True:
            v9, v10, v11 = (0.0, 0.0, 0.0)
            for v12, v13 in a1:
                v14 = v7[0] - v12
                v15 = v7[1] - v13
                v16 = (v14 ** 2 + v15 ** 2) ** 0.5
                if v16 > v8:
                    v9 += v12 / v16
                    v10 += v13 / v16
                    v11 += 1 / v16
            if v11 == 0:
                break
            v17 = [v9 / v11, v10 / v11]
            v14 = abs(v17[0] - v7[0])
            v15 = abs(v17[1] - v7[1])
            v7 = v17
            if v14 * v1 < v8 and v15 * v1 < v8:
                break
        v18 = 0.0
        for v12, v13 in a1:
            v14 = v7[0] - v12
            v15 = v7[1] - v13
            v18 += (v14 ** 2 + v15 ** 2) ** 0.5
        return v18
