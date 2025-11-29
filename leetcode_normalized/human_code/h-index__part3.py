class C1(object):

    def hIndex(self, a1):
        """
        """
        return sum((x >= i + 1 for v1, v2 in enumerate(sorted(a1, reverse=True))))
