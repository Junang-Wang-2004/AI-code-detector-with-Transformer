class C1(object):

    def minNumber(self, a1, a2):
        """
        """
        v1 = set(a1) & set(a2)
        if v1:
            return min(v1)
        v2, v3 = (min(a1), min(a2))
        if v2 > v3:
            v2, v3 = (v3, v2)
        return 10 * v2 + v3
