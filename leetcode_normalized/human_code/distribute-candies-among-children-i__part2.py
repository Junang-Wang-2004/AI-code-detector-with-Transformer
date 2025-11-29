class C1(object):

    def distributeCandies(self, a1, a2):
        """
        """
        return sum((min(a2, a1 - i) - max(a1 - i - a2, 0) + 1 for v1 in range(max(a1 - 2 * a2, 0), min(a2, a1) + 1)))
