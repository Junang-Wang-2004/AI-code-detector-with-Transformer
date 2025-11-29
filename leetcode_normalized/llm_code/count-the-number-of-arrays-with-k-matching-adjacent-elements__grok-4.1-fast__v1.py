class C1:

    def countGoodArrays(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        v2 = a1 - 1
        if a3 < 0 or a3 > v2:
            return 0
        v3 = [1] * (v2 + 1)
        for v4 in range(1, v2 + 1):
            v3[v4] = v3[v4 - 1] * v4 % v1
        v5 = pow(v3[a3], v1 - 2, v1)
        v6 = pow(v3[v2 - a3], v1 - 2, v1)
        v7 = v3[v2] * v5 % v1 * v6 % v1
        v8 = a2 * pow(a2 - 1, v2 - a3, v1) % v1
        return v7 * v8 % v1
