class C1:

    def numberOfWays(self, a1, a2, a3, a4, a5):
        v1 = 10 ** 9 + 7
        v2 = 4

        def multiply(a1, a2):
            v1 = [[0] * v2 for v2 in range(v2)]
            for v3 in range(v2):
                for v4 in range(v2):
                    for v5 in range(v2):
                        v1[v3][v4] = (v1[v3][v4] + a1[v3][v5] * a2[v5][v4]) % v1
            return v1

        def power(a1, a2):
            v1 = [[1 if i == j else 0 for v2 in range(v2)] for v3 in range(v2)]
            while a2 > 0:
                if a2 & 1:
                    v1 = multiply(v1, a1)
                a1 = multiply(a1, a1)
                a2 >>= 1
            return v1
        v3 = [[0, a2 - 1, a1 - 1, 0], [1, a2 - 2, 0, a1 - 1], [1, 0, a1 - 2, a2 - 1], [0, 1, 1, a1 + a2 - 4]]
        v4 = power(v3, a3)
        v5, v6 = a4
        v7, v8 = a5
        if v5 == v7 and v6 == v8:
            v9 = [1, 0, 0, 0]
        elif v5 == v7:
            v9 = [0, 1, 0, 0]
        elif v6 == v8:
            v9 = [0, 0, 1, 0]
        else:
            v9 = [0, 0, 0, 1]
        v10 = 0
        for v11 in range(v2):
            v10 = (v10 + v9[v11] * v4[v11][0]) % v1
        return v10
