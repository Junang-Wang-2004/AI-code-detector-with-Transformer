import collections

class C1(object):

    def longestPalindrome(self, a1):
        """
        """
        v1 = 0
        for v2, v3 in collections.Counter(a1).items():
            v1 += v3 & 1
        return len(a1) - v1 + int(v1 > 0)

    def longestPalindrome2(self, a1):
        """
        """
        v1 = sum([x & 1 for v2 in list(collections.Counter(a1).values())])
        return len(a1) - v1 + int(v1 > 0)
