class C1(object):

    def palindromePartition(self, a1, a2):
        v1 = len(a1)
        v2 = 10 ** 9
        v3 = [[0] * v1 for v4 in range(v1)]
        for v5 in range(v1 - 1):
            v3[v5][v5 + 1] = 0 if a1[v5] == a1[v5 + 1] else 1
        for v6 in range(3, v1 + 1):
            for v5 in range(v1 - v6 + 1):
                v7 = v5 + v6 - 1
                v8 = v3[v5 + 1][v7 - 1]
                v3[v5][v7] = v8 if a1[v5] == a1[v7] else v8 + 1
        v9 = [[v2] * (v1 + 1) for v4 in range(a2 + 1)]
        v9[0][0] = 0
        for v10 in range(1, a2 + 1):
            for v11 in range(v10, v1 + 1):
                for v12 in range(v10 - 1, v11):
                    v13 = v9[v10 - 1][v12]
                    if v13 < v2:
                        v14 = v3[v12][v11 - 1]
                        v9[v10][v11] = min(v9[v10][v11], v13 + v14)
        return v9[a2][v1]
