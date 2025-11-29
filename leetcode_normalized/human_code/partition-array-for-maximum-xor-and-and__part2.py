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
        v3 = 0
        for v4 in range(1, 1 << v2):
            v5 = -1
            v6 = 0
            for v7 in range(v2):
                if v4 & 1 << v7:
                    v5 = v5 & a1[v7] if v5 != -1 else a1[v7]
                else:
                    v6 ^= a1[v7]
            v8 = max_xor_subset((a1[v7] & ~v6 for v7 in range(v2) if not v4 & 1 << v7))
            v3 = max(v3, v5 + v6 + 2 * v8)
        return v3
