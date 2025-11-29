class C1(object):

    def longestString(self, a1, a2, a3):
        """
        """
        return (min(a1, a2) * 2 + int(a1 != a2) + a3) * 2
