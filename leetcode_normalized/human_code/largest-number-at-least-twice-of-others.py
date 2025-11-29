class C1(object):

    def dominantIndex(self, a1):
        """
        """
        v1 = max(a1)
        if all((v1 >= 2 * x for v2 in a1 if v2 != v1)):
            return a1.index(v1)
        return -1
