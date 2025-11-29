class C1(object):

    def timeRequiredToBuy(self, a1, a2):
        """
        """
        return sum((min(x, a1[a2] if i <= a2 else a1[a2] - 1) for v1, v2 in enumerate(a1)))
