class C1(object):

    def stoneGameV(self, a1):
        """
        """
        v1 = len(a1)
        v2 = [0]
        for v3 in a1:
            v2.append(v2[-1] + v3)
        v4 = [[0] * v1 for v5 in range(v1)]
        for v6 in range(1, v1 + 1):
            for v7 in range(v1 - v6 + 1):
                v8 = v7 + v6 - 1
                v9 = v7 if v6 == 1 else v4[v7][v8 - 1]
                while v2[v9] - v2[v7] < v2[v8 + 1] - v2[v9]:
                    v9 += 1
                v4[v7][v8] = v9
        v10 = [[0] * v1 for v5 in range(v1)]
        for v7 in range(v1):
            v10[v7][v7] = a1[v7]
        v11 = [[0] * v1 for v5 in range(v1)]
        for v6 in range(2, v1 + 1):
            for v7 in range(v1 - v6 + 1):
                v8 = v7 + v6 - 1
                v9 = v4[v7][v8]
                v12 = 0
                if v2[v9] - v2[v7] == v2[v8 + 1] - v2[v9]:
                    v12 = max(v10[v7][v9 - 1], v10[v8][v9])
                else:
                    if v7 <= v9 - 2:
                        v12 = max(v12, v10[v7][v9 - 2])
                    if v9 <= v8:
                        v12 = max(v12, v10[v8][v9])
                v11[v7][v8] = v12
                v10[v7][v8] = max(v10[v7][v8 - 1], v2[v8 + 1] - v2[v7] + v12)
                v10[v8][v7] = max(v10[v8][v7 + 1], v2[v8 + 1] - v2[v7] + v12)
        return v11[0][v1 - 1]
