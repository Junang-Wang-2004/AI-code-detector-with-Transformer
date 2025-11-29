class C1(object):

    def maxTrailingZeros(self, a1):

        def count_factors(a1):
            if a1 == 0:
                return (0, 0)
            v1 = 0
            while a1 % 2 == 0:
                v1 += 1
                a1 //= 2
            v3 = 0
            while a1 % 5 == 0:
                v3 += 1
                a1 //= 5
            return (v1, v3)
        if not a1 or not a1[0]:
            return 0
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = [[(0, 0) for v4 in range(v2)] for v4 in range(v1)]
        for v5 in range(v1):
            v3[v5][0] = count_factors(a1[v5][0])
            for v6 in range(1, v2):
                v7 = count_factors(a1[v5][v6])
                v3[v5][v6] = (v3[v5][v6 - 1][0] + v7[0], v3[v5][v6 - 1][1] + v7[1])
        v8 = [[(0, 0) for v4 in range(v2)] for v4 in range(v1)]
        for v5 in range(v1):
            v8[v5][v2 - 1] = count_factors(a1[v5][v2 - 1])
            for v6 in range(v2 - 2, -1, -1):
                v7 = count_factors(a1[v5][v6])
                v8[v5][v6] = (v8[v5][v6 + 1][0] + v7[0], v8[v5][v6 + 1][1] + v7[1])
        v9 = [[(0, 0) for v4 in range(v1)] for v4 in range(v2)]
        for v6 in range(v2):
            for v5 in range(1, v1):
                v7 = count_factors(a1[v5 - 1][v6])
                v9[v6][v5] = (v9[v6][v5 - 1][0] + v7[0], v9[v6][v5 - 1][1] + v7[1])
        v10 = [[(0, 0) for v4 in range(v1)] for v4 in range(v2)]
        for v6 in range(v2):
            for v5 in range(v1 - 2, -1, -1):
                v7 = count_factors(a1[v5 + 1][v6])
                v10[v6][v5] = (v10[v6][v5 + 1][0] + v7[0], v10[v6][v5 + 1][1] + v7[1])
        v11 = 0
        for v5 in range(v1):
            for v6 in range(v2):
                v12, v13 = (v3[v5][v6][0] + v9[v6][v5][0], v3[v5][v6][1] + v9[v6][v5][1])
                v11 = max(v11, min(v12, v13))
                v12, v13 = (v8[v5][v6][0] + v9[v6][v5][0], v8[v5][v6][1] + v9[v6][v5][1])
                v11 = max(v11, min(v12, v13))
                v12, v13 = (v3[v5][v6][0] + v10[v6][v5][0], v3[v5][v6][1] + v10[v6][v5][1])
                v11 = max(v11, min(v12, v13))
                v12, v13 = (v8[v5][v6][0] + v10[v6][v5][0], v8[v5][v6][1] + v10[v6][v5][1])
                v11 = max(v11, min(v12, v13))
        return v11
