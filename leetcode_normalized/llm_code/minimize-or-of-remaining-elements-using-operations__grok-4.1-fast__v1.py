class C1:

    def minOrAfterOperations(self, a1, a2):
        if not a1:
            return 0
        v1 = max(a1).bit_length()
        v2 = (1 << v1) - 1
        v3 = 0
        for v4 in range(v1 - 1, -1, -1):
            v3 <<= 1
            v5 = v2
            v6 = 0
            for v7 in a1:
                v5 &= v7 >> v4
                if v5 & ~v3:
                    v6 += 1
                else:
                    v5 = v2
            if v6 > a2:
                v3 |= 1
        return v3
