class C1(object):

    def numberOfPairs(self, a1):
        """
        """
        v1 = [0] * (max(a1) + 1)
        v2 = 0
        for v3 in a1:
            v1[v3] ^= 1
            if not v1[v3]:
                v2 += 1
        return [v2, len(a1) - 2 * v2]
