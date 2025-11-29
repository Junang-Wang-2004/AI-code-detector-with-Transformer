import collections

class C1(object):

    def longestPalindrome(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2 = v3 = 0
        for v4, v5 in v1.items():
            if v4 == v4[::-1]:
                v2 += v5 // 2
                v3 |= v5 % 2
            elif v4 < v4[::-1] and v4[::-1] in v1:
                v2 += min(v5, v1[v4[::-1]])
        return v2 * 4 + v3 * 2
