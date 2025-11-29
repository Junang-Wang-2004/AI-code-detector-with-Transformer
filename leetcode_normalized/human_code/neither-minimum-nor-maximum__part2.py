class C1(object):

    def findNonMinOrMax(self, a1):
        """
        """
        v1, v2 = (max(a1), min(a1))
        return next((x for v3 in a1 if v3 not in (v1, v2)), -1)
