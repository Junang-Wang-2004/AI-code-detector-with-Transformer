class C1:

    def countCoprime(self, a1):
        v1 = 10 ** 9 + 7
        v2 = max((max(r) for v3 in a1))
        v4 = list(range(v2 + 1))
        for v5 in range(2, int(v2 ** 0.5) + 1):
            if v4[v5] == v5:
                for v6 in range(v5 * v5, v2 + 1, v5):
                    if v4[v6] == v6:
                        v4[v6] = v5
        v7 = [0] * (v2 + 1)
        v7[1] = 1
        for v5 in range(2, v2 + 1):
            v8 = v4[v5]
            v9 = v5 // v8
            if v9 % v8 == 0:
                v7[v5] = 0
            else:
                v7[v5] = -v7[v9]
        v10 = [1] * (v2 + 1)
        for v3 in a1:
            v11 = [0] * (v2 + 1)
            for v12 in v3:
                v11[v12] += 1
            v13 = [0] * (v2 + 1)
            for v14 in range(1, v2 + 1):
                v15 = 0
                v16 = v14
                while v16 <= v2:
                    v15 = (v15 + v11[v16]) % v1
                    v16 += v14
                v13[v14] = v15
            for v14 in range(1, v2 + 1):
                v10[v14] = v10[v14] * v13[v14] % v1
        v17 = 0
        for v14 in range(1, v2 + 1):
            v17 = (v17 + v7[v14] * v10[v14]) % v1
        return v17
