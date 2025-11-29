class C1(object):

    def maximizeXorAndXor(self, a1):
        """
        """

        def max_xor_subset(a1):
            v1 = [0] * l
            for v2 in a1:
                for v3 in reversed(range(len(v1))):
                    if not v2 & 1 << v3:
                        continue
                    if v1[v3] == 0:
                        v1[v3] = v2
                        break
                    v2 ^= v1[v3]
            v4 = 0
            for v5 in reversed(v1):
                if v4 ^ v5 > v4:
                    v4 ^= v5
            return v4
        v1 = max(a1).bit_length()
        v2 = len(a1)
        v3 = [0] * (1 << v2)
        v4 = [0] * (1 << v2)
        for v5 in range(1, 1 << v2):
            v6 = v5 & -v5
            v7 = v6.bit_length() - 1
            v3[v5] = v3[v5 ^ v6] & a1[v7] if v5 ^ v6 else a1[v7]
            v4[v5] = v4[v5 ^ v6] ^ a1[v7]
        v8 = 0
        v9 = (1 << v2) - 1
        for v5 in range(1, 1 << v2):
            v10 = v3[v5]
            v11 = v4[v9 ^ v5]
            v12 = max_xor_subset((a1[v7] & ~v11 for v7 in range(v2) if not v5 & 1 << v7))
            v8 = max(v8, v10 + v11 + 2 * v12)
        return v8
