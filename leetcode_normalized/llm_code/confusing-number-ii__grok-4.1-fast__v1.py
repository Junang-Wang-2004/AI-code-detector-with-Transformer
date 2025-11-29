class C1:

    def confusingNumberII(self, a1):
        if a1 < 1:
            return 0
        v1 = str(a1)
        v2 = len(v1)
        v3 = [0, 1, 6, 8, 9]
        v4 = [1, 6, 8, 9]
        v5 = [0, 1, 8]
        v6 = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        v7 = 0
        v8 = 1
        for v9 in range(v2 - 1):
            v7 += 4 * v8
            v8 *= 5
        v10 = 0
        v11 = 5 ** (v2 - 1)
        v12 = True
        for v13 in range(v2):
            if not v12:
                break
            v14 = int(v1[v13])
            v15 = 1 if v13 == 0 else 0
            v16 = sum((1 for v17 in v3 if v17 >= v15 and v17 < v14))
            v10 += v16 * v11
            if v14 not in v6:
                v12 = False
            v11 //= 5
        if v12:
            v10 += 1
        v18 = v7 + v10
        v19 = []

        def build(a1, a2, a3):
            if len(a1) == a2:
                if a3 and a1[-1] not in v5:
                    return
                v1 = a1[:-1] if a3 else a1
                v2 = [v6[d] for v3 in reversed(v1)]
                v4 = v1 + ([a1[-1]] if a3 else []) + v2
                v5 = 0
                for v6 in v4:
                    v5 = v5 * 10 + v6
                v19.append(v5)
                return
            v7 = v4 if not a1 else v3
            for v3 in v7:
                build(a1 + [v3], a2, a3)
        for v20 in range(1, 11):
            v21 = (v20 + 1) // 2
            v22 = v20 % 2 == 1
            build([], v21, v22)
        v23 = sum((1 for v24 in v19 if v24 <= a1))
        return v18 - v23
