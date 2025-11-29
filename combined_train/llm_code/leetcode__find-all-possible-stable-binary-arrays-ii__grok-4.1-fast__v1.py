class C1(object):

    def numberOfStableArrays(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        v2 = [[[0] * 2 for v3 in range(a2 + 1)] for v3 in range(a1 + 1)]
        v4 = [[[[0] * (a3 + 1) for v3 in range(2)] for v3 in range(a2 + 1)] for v3 in range(a1 + 1)]
        v2[0][0][0] = 1
        v2[0][0][1] = 1
        for v5 in range(a1 + 1):
            for v6 in range(a2 + 1):
                if v5 == 0 and v6 == 0:
                    continue
                if v5 > 0:
                    v4[v5][v6][0][1] = v2[v5 - 1][v6][1]
                    for v7 in range(2, a3 + 1):
                        v4[v5][v6][0][v7] = v4[v5 - 1][v6][0][v7 - 1]
                if v6 > 0:
                    v4[v5][v6][1][1] = v2[v5][v6 - 1][0]
                    for v7 in range(2, a3 + 1):
                        v4[v5][v6][1][v7] = v4[v5][v6 - 1][1][v7 - 1]
                v2[v5][v6][0] = sum(v4[v5][v6][0][1:]) % v1
                v2[v5][v6][1] = sum(v4[v5][v6][1][1:]) % v1
        return (v2[a1][a2][0] + v2[a1][a2][1]) % v1
