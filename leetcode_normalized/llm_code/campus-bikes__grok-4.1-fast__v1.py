class C1(object):

    def assignBikes(self, a1, a2):
        v1 = len(a1)
        v2 = 1 << v1
        v3 = 10 ** 9 + 7
        v4 = [[0] * v1 for v5 in range(v1)]
        for v6 in range(v1):
            for v7 in range(v1):
                v4[v6][v7] = abs(a1[v6][0] - a2[v7][0]) + abs(a1[v6][1] - a2[v7][1])
        v8 = [bin(m).count('1') for v9 in range(v2)]
        v10 = [v3] * v2
        v10[0] = 0
        for v11 in range(1, v2):
            v12 = v8[v11] - 1
            for v13 in range(v1):
                if v11 & 1 << v13:
                    v14 = v11 ^ 1 << v13
                    v10[v11] = min(v10[v11], v10[v14] + v4[v12][v13])
        v15 = [-1] * v1
        v11 = v2 - 1
        for v6 in range(v1 - 1, -1, -1):
            for v7 in range(v1):
                if v11 & 1 << v7:
                    v14 = v11 ^ 1 << v7
                    if v10[v11] == v10[v14] + v4[v6][v7]:
                        v15[v6] = v7
                        v11 = v14
                        break
        return v15
