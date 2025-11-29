class C1(object):

    def maxXorSubsequences(self, a1):
        """
        """

        def max_xor_subset(a1):
            v1 = [0] * l
            for v2 in a1:
                for v3 in v1:
                    if v2 ^ v3 < v2:
                        v2 ^= v3
                if v2:
                    v1.append(v2)
            v4 = 0
            for v3 in v1:
                if v4 ^ v3 > v4:
                    v4 ^= v3
            return v4
        v1 = max(a1).bit_length()
        return max_xor_subset(a1)
