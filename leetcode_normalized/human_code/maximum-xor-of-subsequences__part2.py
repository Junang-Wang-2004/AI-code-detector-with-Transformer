class C1(object):

    def maxXorSubsequences(self, a1):
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
        return max_xor_subset(a1)
