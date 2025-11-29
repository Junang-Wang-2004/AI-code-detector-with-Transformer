class C1(object):

    def appealSum(self, a1):
        """
        """
        v1 = v2 = 0
        v3 = [-1] * 26
        for v4, v5 in enumerate(a1):
            v2 += v4 - v3[ord(v5) - ord('a')]
            v3[ord(v5) - ord('a')] = v4
            v1 += v2
        return v1
