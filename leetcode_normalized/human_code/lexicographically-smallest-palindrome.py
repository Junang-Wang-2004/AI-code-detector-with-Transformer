class C1(object):

    def makeSmallestPalindrome(self, a1):
        """
        """
        return ''.join((min(a1[i], a1[~i]) for v1 in range(len(a1))))
