class C1:

    def numTilings(self, a1):
        v1 = 10 ** 9 + 7

        def multiply(a1, a2):
            v1 = len(a1)
            v2 = len(a2[0])
            v3 = len(a1[0])
            v4 = [[0] * v2 for v5 in range(v1)]
            for v6 in range(v1):
                for v7 in range(v2):
                    for v8 in range(v3):
                        v4[v6][v7] = (v4[v6][v7] + a1[v6][v8] * a2[v8][v7]) % v1
            return v4

        def power(a1, a2):
            v1 = len(a1)
            v2 = [[1 if i == j else 0 for v3 in range(v1)] for v4 in range(v1)]
            while a2 > 0:
                if a2 % 2 == 1:
                    v2 = multiply(v2, a1)
                a1 = multiply(a1, a1)
                a2 //= 2
            return v2
        if a1 == 1:
            return 1
        if a1 == 2:
            return 2
        v2 = [[2, 0, 1], [1, 0, 0], [0, 1, 0]]
        v3 = [[2], [1], [1]]
        v4 = power(v2, a1 - 2)
        v5 = multiply(v4, v3)
        return v5[0][0]
