class C1:

    def zigZagArrays(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        v2 = a3 - a2 + 1
        v3 = [[1 if i + j < v2 - 1 else 0 for v4 in range(v2)] for v5 in range(v2)]

        def mul_mat(a1, a2):
            v1 = len(a1)
            v2 = len(a1[0])
            v3 = len(a2)
            v4 = len(a2[0])
            v5 = [[0] * v4 for v6 in range(v1)]
            for v7 in range(v1):
                for v8 in range(v4):
                    v9 = 0
                    for v10 in range(v2):
                        v9 = (v9 + a1[v7][v10] * a2[v10][v8]) % v1
                    v5[v7][v8] = v9
            return v5

        def pow_mat(a1, a2):
            v1 = len(a1)
            v2 = [[1 if x == y else 0 for v3 in range(v1)] for v4 in range(v1)]
            while a2 > 0:
                if a2 & 1:
                    v2 = mul_mat(v2, a1)
                a1 = mul_mat(a1, a1)
                a2 >>= 1
            return v2
        v6 = [[1] * v2]
        if a1 == 1:
            v7 = sum(v6[0]) % v1
        else:
            v8 = pow_mat(v3, a1 - 1)
            v9 = mul_mat(v6, v8)
            v7 = sum(v9[0]) % v1
        return v7 * 2 % v1
