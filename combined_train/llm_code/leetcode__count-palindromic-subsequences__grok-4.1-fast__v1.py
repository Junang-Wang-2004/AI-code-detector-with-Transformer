class C1(object):

    def countPalindromes(self, a1):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = [[] for v4 in range(10)]
        for v5 in range(v2):
            v3[int(a1[v5])].append(v5)
        v6 = 0
        for v7 in range(10):
            v8 = v3[v7]
            v9 = len(v8)
            if v9 < 2:
                continue
            for v10 in range(10):
                v11 = v3[v10]
                v12 = len(v11)
                v13 = [0] * v9
                v14 = [0] * v9
                v15 = 0
                for v16 in range(v9):
                    while v15 < v12 and v11[v15] < v8[v16]:
                        v15 += 1
                    v13[v16] = v15
                v17 = 0
                for v16 in range(v9):
                    while v17 < v12 and v11[v17] <= v8[v16]:
                        v17 += 1
                    v14[v16] = v12 - v17
                v18 = [0] * (v9 + 1)
                for v19 in range(v9 - 1, -1, -1):
                    v18[v19] = (v18[v19 + 1] + v14[v19]) % v1
                for v20 in range(v9 - 1):
                    v21 = v13[v20] * v18[v20 + 1] % v1
                    v6 = (v6 + v21) % v1
        return v6
