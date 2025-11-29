class C1(object):

    def countBalancedPermutations(self, a1):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = sum((int(d) for v4 in a1))
        if v3 % 2 != 0:
            return 0
        v5 = v3 // 2
        v6 = v2 // 2
        v7 = v2 - v6
        v8 = [0] * 10
        for v9 in a1:
            v8[int(v9)] += 1
        v10 = [1] * (v2 + 1)
        for v11 in range(1, v2 + 1):
            v10[v11] = v10[v11 - 1] * v11 % v1

        def inverse(a1):
            return pow(a1, v1 - 2, v1)
        v12 = [inverse(v10[v11]) for v11 in range(v2 + 1)]

        def choose(a1, a2):
            if a2 < 0 or a2 > a1:
                return 0
            return v10[a1] * v12[a2] % v1 * v12[a1 - a2] % v1
        v13 = [[0] * (v6 + 1) for v14 in range(v5 + 1)]
        v13[0][0] = 1
        for v4 in range(10):
            if v8[v4] == 0:
                continue
            v15 = [[0] * (v6 + 1) for v14 in range(v5 + 1)]
            for v16 in range(v5 + 1):
                for v17 in range(v6 + 1):
                    if v13[v16][v17] == 0:
                        continue
                    for v18 in range(v8[v4] + 1):
                        v19 = v16 + v18 * v4
                        v20 = v17 + v18
                        if v19 > v5 or v20 > v6:
                            break
                        v15[v19][v20] = (v15[v19][v20] + v13[v16][v17] * choose(v8[v4], v18)) % v1
            v13 = v15
        v21 = v13[v5][v6]
        v21 = v21 * v10[v6] % v1
        v21 = v21 * v10[v7] % v1
        for v22 in v8:
            v21 = v21 * v12[v22] % v1
        return v21
