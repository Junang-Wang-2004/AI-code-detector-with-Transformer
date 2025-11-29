class C1(object):

    def semiOrderedPermutation(self, a1):
        """
        """
        v1, v2 = (a1.index(1), a1.index(len(a1)))
        return v1 + (len(a1) - 1 - v2) - int(v1 > v2)
