class C1:

    def distinctSequences(self, a1):
        if a1 == 1:
            return 6
        v1 = 10 ** 9 + 7

        def compute_gcd(a1, a2):
            while a2 != 0:
                a1, a2 = (a2, a1 % a2)
            return a1
        v2 = 6
        v3 = [[0] * v2 for v4 in range(v2)]
        for v5 in range(v2):
            for v6 in range(v2):
                if v5 != v6 and compute_gcd(v5 + 1, v6 + 1) == 1:
                    v3[v5][v6] = 1
        v7 = [[0] * v2 for v4 in range(v2)]
        for v8 in range(v2):
            for v9 in range(v2):
                v7[v8][v9] = v3[v8][v9]
        for v4 in range(a1 - 2):
            v10 = [[0] * v2 for v4 in range(v2)]
            for v11 in range(v2):
                for v12 in range(v2):
                    v13 = v7[v11][v12]
                    if v13 == 0:
                        continue
                    for v14 in range(v2):
                        if v3[v12][v14] == 1 and v11 != v14:
                            v10[v12][v14] = (v10[v12][v14] + v13) % v1
            v7 = v10
        v15 = 0
        for v16 in v7:
            for v17 in v16:
                v15 = (v15 + v17) % v1
        return v15
