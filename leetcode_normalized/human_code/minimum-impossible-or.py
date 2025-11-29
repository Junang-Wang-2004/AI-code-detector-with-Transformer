class C1(object):

    def minImpossibleOR(self, a1):
        """
        """
        v1 = set(a1)
        return next((1 << i for v2 in range(31) if 1 << v2 not in v1))
