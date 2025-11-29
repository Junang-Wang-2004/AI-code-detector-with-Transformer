class C1:

    def minNonZeroProduct(self, a1: int) -> int:
        v1 = 10 ** 9 + 7
        v2 = v1 - 1
        v3 = pow(2, a1 - 1, v2)
        v4 = (v3 - 1 + v2) % v2
        v5 = pow(2, a1, v1)
        v6 = (v5 - 1 + v1) % v1
        v7 = (v5 - 2 + v1) % v1
        v8 = pow(v7, v4, v1)
        return v6 * v8 % v1
