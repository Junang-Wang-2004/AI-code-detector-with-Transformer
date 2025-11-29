class C1:

    def tripletCount(self, a1, a2, a3):

        def bit_parity(a1):
            a1 ^= a1 >> 32
            a1 ^= a1 >> 16
            a1 ^= a1 >> 8
            a1 ^= a1 >> 4
            a1 ^= a1 >> 2
            a1 ^= a1 >> 1
            return a1 & 1
        v1 = sum((bit_parity(x) for v2 in a1))
        v3 = len(a1) - v1
        v4 = sum((bit_parity(v2) for v2 in a2))
        v5 = len(a2) - v4
        v6 = sum((bit_parity(v2) for v2 in a3))
        v7 = len(a3) - v6
        v8 = len(a1) * len(a2) * len(a3)
        v9 = v1 * v5 * v7 + v3 * v4 * v7 + v3 * v5 * v6 + v1 * v4 * v6
        return v8 - v9
