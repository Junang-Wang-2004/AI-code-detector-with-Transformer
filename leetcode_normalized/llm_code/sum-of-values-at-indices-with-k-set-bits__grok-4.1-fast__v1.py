class C1:

    def sumIndicesWithKSetBits(self, a1, a2):
        v1 = len(a1)
        v2 = 0

        def build_comb(a1, a2, a3):
            nonlocal total_sum
            if a2 == 0:
                if a3 < v1:
                    v1 += a1[a3]
                return
            for v2 in range(a1, 32):
                v3 = a3 | 1 << v2
                if v3 >= v1:
                    break
                build_comb(v2 + 1, a2 - 1, v3)
        build_comb(0, a2, 0)
        return v2
