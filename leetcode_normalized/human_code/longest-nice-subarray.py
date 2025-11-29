class C1(object):

    def longestNiceSubarray(self, a1):
        """
        """
        v1 = v2 = v3 = 0
        for v4 in range(len(a1)):
            while v3 & a1[v4]:
                v3 ^= a1[v2]
                v2 += 1
            v3 |= a1[v4]
            v1 = max(v1, v4 - v2 + 1)
        return v1
