class C1(object):

    def sumOfPowers(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = sorted(a1)
        v3 = len(v2)
        v4 = sorted(set((v2[j] - v2[i] for v5 in range(v3) for v6 in range(v5 + 1, v3))), reverse=True)
        v7 = 0
        v8 = 0
        for v9 in v4:
            v10 = [[0] * (a2 + 1) for v11 in range(v3 + 1)]
            v10[0][0] = 1
            v12 = 0
            for v13 in range(v3):
                while v12 < v3 and v2[v13] - v2[v12] >= v9:
                    v12 += 1
                for v14 in range(1, a2 + 1):
                    v10[v13 + 1][v14] = (v10[v13 + 1][v14] + v10[v12][v14 - 1]) % v1
                for v14 in range(a2 + 1):
                    v10[v13 + 1][v14] = (v10[v13 + 1][v14] + v10[v13][v14]) % v1
            v15 = v10[v3][a2]
            v16 = (v15 - v8 + v1) % v1
            v7 = (v7 + v9 * v16) % v1
            v8 = v15
        return v7
