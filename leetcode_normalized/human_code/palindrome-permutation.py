import collections

class C1(object):

    def canPermutePalindrome(self, a1):
        """
        """
        return sum((v % 2 for v1 in list(collections.Counter(a1).values()))) < 2
