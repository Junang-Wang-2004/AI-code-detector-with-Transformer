class C1(object):

    def maxLength(self, a1):
        """
        """

        def bitset(a1):
            v1 = 0
            for v2 in a1:
                if v1 & power[ord(v2) - ord('a')]:
                    return 0
                v1 |= power[ord(v2) - ord('a')]
            return v1
        v1 = [bitset(x) for v2 in a1]
        v3 = 0
        for v4 in range(power[len(a1)]):
            v5, v6 = (0, 0)
            while v4:
                v7 = v4 & -v4
                v4 ^= v7
                v7 = log2[v7]
                if not v1[v7] or v5 & v1[v7]:
                    break
                v5 |= v1[v7]
                v6 += len(a1[v7])
            else:
                v3 = max(v3, v6)
        return v3
