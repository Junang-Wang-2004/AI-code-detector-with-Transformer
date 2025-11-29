class C1:

    def numberOfStableArrays(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        v2 = [[0] * (a2 + 1) for v3 in range(a1 + 1)]
        v4 = [[0] * (a2 + 1) for v3 in range(a1 + 1)]
        for v5 in range(a1 + 1):
            v2[v5][0] = 1 if v5 <= a3 else 0
        for v6 in range(a2 + 1):
            v4[0][v6] = 1 if v6 <= a3 else 0
        for v5 in range(1, a1 + 1):
            for v6 in range(1, a2 + 1):
                v2[v5][v6] = (v2[v5 - 1][v6] + v4[v5 - 1][v6]) % v1
                if v5 > a3:
                    v2[v5][v6] = (v2[v5][v6] - v4[v5 - a3 - 1][v6]) % v1
                v4[v5][v6] = (v2[v5][v6 - 1] + v4[v5][v6 - 1]) % v1
                if v6 > a3:
                    v4[v5][v6] = (v4[v5][v6] - v2[v5][v6 - a3 - 1]) % v1
        return (v2[a1][a2] + v4[a1][a2]) % v1
