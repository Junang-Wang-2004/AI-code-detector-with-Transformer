import collections

class C1(object):

    def distinctSubseqII(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = (0, [0] * 26)
        for v4 in a1:
            v2, v3[ord(v4) - ord('a')] = ((v2 + (v2 + 1 - v3[ord(v4) - ord('a')])) % v1, (v2 + 1) % v1)
        return v2
