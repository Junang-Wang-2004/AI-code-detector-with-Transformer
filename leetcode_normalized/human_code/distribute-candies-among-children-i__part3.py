class C1(object):

    def distributeCandies(self, a1, a2):
        """
        """
        return sum((a1 - i - j <= a2 for v1 in range(min(a2, a1) + 1) for v2 in range(min(a2, a1 - v1) + 1)))
