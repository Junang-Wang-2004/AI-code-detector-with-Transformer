class C1(object):

    def stoneGameV(self, a1):
        """
        """
        v1 = len(a1)
        v2 = [0]
        for v3 in a1:
            v2.append(v2[-1] + v3)
        v4 = list(range(v1))
        v5 = [[0] * v1 for v6 in range(v1)]
        for v7 in range(v1):
            v5[v7][v7] = a1[v7]
        v8 = 0
        for v9 in range(2, v1 + 1):
            for v7 in range(v1 - v9 + 1):
                v10 = v7 + v9 - 1
                while v2[v4[v7]] - v2[v7] < v2[v10 + 1] - v2[v4[v7]]:
                    v4[v7] += 1
                v11 = v4[v7]
                v8 = 0
                if v2[v11] - v2[v7] == v2[v10 + 1] - v2[v11]:
                    v8 = max(v5[v7][v11 - 1], v5[v10][v11])
                else:
                    if v7 <= v11 - 2:
                        v8 = max(v8, v5[v7][v11 - 2])
                    if v11 <= v10:
                        v8 = max(v8, v5[v10][v11])
                v5[v7][v10] = max(v5[v7][v10 - 1], v2[v10 + 1] - v2[v7] + v8)
                v5[v10][v7] = max(v5[v10][v7 + 1], v2[v10 + 1] - v2[v7] + v8)
        return v8
