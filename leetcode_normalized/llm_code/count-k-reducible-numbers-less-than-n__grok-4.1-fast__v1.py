class C1:

    def countKReducibleNumbers(self, a1: str, a2: int) -> int:
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = [0] * v2
        for v4 in range(2, v2):
            v5 = 0
            v6 = v4
            while v6:
                v5 += v6 & 1
                v6 >>= 1
            v3[v4] = v3[v5] + 1
        v7 = [1] * (v2 + 1)
        for v4 in range(1, v2 + 1):
            v7[v4] = v7[v4 - 1] * v4 % v1
        v8 = [0] * (v2 + 1)
        v8[v2] = pow(v7[v2], v1 - 2, v1)
        for v4 in range(v2 - 1, -1, -1):
            v8[v4] = v8[v4 + 1] * (v4 + 1) % v1

        def comb(a1, a2):
            if a2 < 0 or a2 > a1:
                return 0
            return v7[a1] * v8[a2] % v1 * v8[a1 - a2] % v1
        v9 = 0
        v10 = 0
        for v4 in range(v2):
            if a1[v4] == '1':
                v11 = v2 - v4 - 1
                for v12 in range(v11 + 1):
                    v13 = v10 + v12
                    if v13 < v2 and v3[v13] < a2:
                        v9 = (v9 + comb(v11, v12)) % v1
                v10 += 1
        return (v9 - 1) % v1
