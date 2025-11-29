class C1(object):

    def numOfSubarrays(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = (0, 0)
        v4 = [1, 0]
        for v5 in a1:
            v3 ^= v5 & 1
            v4[v3] += 1
            v2 = (v2 + v4[v3 ^ 1]) % v1
        return v2
