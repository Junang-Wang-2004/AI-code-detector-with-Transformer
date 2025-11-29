class C1(object):

    def minimumCost(self, a1):
        """
        """
        a1.sort(reverse=True)
        return sum((x for v1, v2 in enumerate(a1) if v1 % 3 != 2))
