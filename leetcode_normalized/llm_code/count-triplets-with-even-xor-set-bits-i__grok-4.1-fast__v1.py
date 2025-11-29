class C1:

    def tripletCount(self, a1, a2, a3):

        def bit_parity(a1):
            v1 = 0
            while a1:
                v1 ^= a1 & 1
                a1 >>= 1
            return v1

        def parity_counts(a1):
            v1 = 0
            for v2 in a1:
                if bit_parity(v2) == 0:
                    v1 += 1
            return (v1, len(a1) - v1)
        v1, v2 = parity_counts(a1)
        v3, v4 = parity_counts(a2)
        v5, v6 = parity_counts(a3)
        return v1 * v3 * v5 + v2 * v4 * v5 + v2 * v3 * v6 + v1 * v4 * v6
