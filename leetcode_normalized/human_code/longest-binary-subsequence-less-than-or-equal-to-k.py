class C1(object):

    def longestSubsequence(self, a1, a2):
        """
        """
        v1, v2 = (0, 1)
        for v3 in reversed(range(len(a1))):
            if a1[v3] == '0':
                v1 += 1
            elif v2 <= a2:
                a2 -= v2
                v1 += 1
            if v2 <= a2:
                v2 <<= 1
        return v1
