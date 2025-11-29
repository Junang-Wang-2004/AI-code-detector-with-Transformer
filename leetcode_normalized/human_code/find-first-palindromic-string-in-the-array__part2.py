class C1(object):

    def firstPalindrome(self, a1):
        """
        """
        return next((x for v1 in a1 if v1 == v1[::-1]), '')
