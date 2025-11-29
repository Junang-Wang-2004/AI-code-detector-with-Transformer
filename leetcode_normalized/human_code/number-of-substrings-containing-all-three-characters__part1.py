class C1(object):

    def numberOfSubstrings(self, a1):
        """
        """
        v1, v2 = (0, [-1] * 3)
        for v3, v4 in enumerate(a1):
            v2[ord(v4) - ord('a')] = v3
            v1 += min(v2) + 1
        return v1
