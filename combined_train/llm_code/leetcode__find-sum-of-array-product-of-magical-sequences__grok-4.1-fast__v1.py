class C1(object):

    def magicalSum(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        v2 = [1] * (a1 + 1)
        for v3 in range(1, a1 + 1):
            v2[v3] = v2[v3 - 1] * v3 % v1
        v4 = [0] * (a1 + 1)
        v4[a1] = pow(v2[a1], v1 - 2, v1)
        for v3 in range(a1 - 1, -1, -1):
            v4[v3] = v4[v3 + 1] * (v3 + 1) % v1

        def choose(a1, a2):
            if a2 < 0 or a2 > a1:
                return 0
            return v2[a1] * v4[a2] % v1 * v4[a1 - a2] % v1
        v5 = a1 + 1
        v6 = [[[0 for v7 in range(a1 + 1)] for v7 in range(a2 + 1)] for v7 in range(v5)]
        v6[0][0][a1] = 1
        for v8 in a3:
            v9 = [[[0 for v7 in range(a1 + 1)] for v7 in range(a2 + 1)] for v7 in range(v5)]
            for v10 in range(v5):
                for v11 in range(a2 + 1):
                    for v12 in range(a1 + 1):
                        v13 = v6[v10][v11][v12]
                        if v13 == 0:
                            continue
                        v14 = 1
                        for v15 in range(v12 + 1):
                            v16 = v10 + v15
                            v17 = v16 // 2
                            v18 = v11 + v16 % 2
                            if v18 > a2:
                                continue
                            v19 = v12 - v15
                            v20 = v13 * v14 % v1 * choose(v12, v15) % v1
                            v9[v17][v18][v19] = (v9[v17][v18][v19] + v20) % v1
                            v14 = v14 * v8 % v1
            v6 = v9
        v21 = 0
        for v10 in range(v5):
            v22 = bin(v10).count('1')
            v23 = a2 - v22
            if 0 <= v23 <= a2:
                v21 = (v21 + v6[v10][v23][0]) % v1
        return v21
